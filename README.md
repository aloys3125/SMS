 AI powered Smart Meeting Summarizer
The Smart Meeting Summarizer (SMS) is a full-stack web application that uses natural language processing to generate concise summaries from lengthy meeting transcripts. It helps professionals, students, and teams extract essential insights, decisions, and speaker highlights—instantly.
 
Features
AI-Powered Summarization: Uses BART-Large CNN model from Hugging Face.
Real-Time Output: Instant summaries from pasted transcripts.
Export Options: Download summaries as .pdf` or .txt, or copy to clipboard.
Responsive Design: Works smoothly on desktops, tablets, and smartphones.
Dark Mode:Theme toggle for better readability.
No Signup Needed: Paste transcript and summarize—no login required.
Minimalist UI: Clean, distraction-free user experience.

 Tech Stack

 Frontend
 HTML5, CSS3
 JavaScript
 Font Awesome
 Google Fonts
 jsPDF (PDF generation)

 Backend
 Python
 Flask (web server)
 Hugging Face Transformers (BART)
 PyTorch
 NLTK (text preprocessing)

Installation and usage 
 Clone the repo
   ```bash
   git clone https://github.com/aloys3125/SMS.git
   cd SMS
Install dependencies
pip install -r requirements.txt
Run the app
python app.py
Access locally
