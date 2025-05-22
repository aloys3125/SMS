from transformers import pipeline
import re
summarizer = None

def preprocess_text(text):
    if not isinstance(text, str):
        print("Error: Input text must be a string.")
        return ""

    lines = text.split('\n')
    grouped = {}
    for line in lines:
        match = re.match(r"\[.*?\]\s*(\w+):", line)
        if match:
            speaker = match.group(1)
            line = re.sub(r"\[.*?\]\s*\w+:", "", line).strip()
        else:
            speaker = "Unknown"
        grouped.setdefault(speaker, []).append(line)
    combined = [f"{speaker}: {' '.join(speaker_lines)}" for speaker, speaker_lines in grouped.items()]
    return "\n".join(combined)

def generate_summary(text, max_len=120, min_len=30):
    global summarizer

    if not text or not text.strip():
        return "Error: Empty input text."

    cleaned_text = preprocess_text(text)
    if not cleaned_text:
        return "Error: Text preprocessing failed."
     # lazy load 
    if summarizer is None:
        try:
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        except Exception as e:
            return f"Error loading summarization pipeline: {str(e)}"

    try:
        summary = summarizer(cleaned_text, max_length=max_len, min_length=min_len, do_sample=False)
        if isinstance(summary, list) and len(summary) > 0 and "summary_text" in summary[0]:
            summary_text = summary[0]["summary_text"]
        else:
            return "Error: Invalid summarization output."
    except Exception as e:
        return f"Summarization failed: {str(e)}"

    bullets = re.split(r'(?<=[.?!])\s+', summary_text.strip())
    formatted = "\n".join(f"• {line}" for line in bullets if line)
    return formatted
