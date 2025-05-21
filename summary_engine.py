from transformers import pipeline
import re

try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print(f"Error loading summarization pipeline: {e}")
    summarizer = None  # Set to None to prevent further errors

def preprocess_text(text):
    """
    Preprocesses the input text to handle speaker attributions and formatting.

    Args:
        text (str): The input text transcript.

    Returns:
        str: The preprocessed text, or an empty string on error.
    """
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
    """
    Generates a summary of the given text.

    Args:
        text (str): The input text to summarize.
        max_len (int, optional): The maximum length of the summary. Defaults to 120.
        min_len (int, optional): The minimum length of the summary. Defaults to 30.

    Returns:
        str: The formatted summary, or an error message if summarization fails.
    """
    if not text or not text.strip():
        return "Error: Empty input text."

    if summarizer is None:
        return "Error: Summarizer pipeline not loaded."

    cleaned_text = preprocess_text(text)
    if not cleaned_text:  # Check if preprocess_text returned empty string
        return "Error: Text preprocessing failed."

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
