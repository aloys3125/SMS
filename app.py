# sms/app.py


from flask import Flask, render_template, request
from summary_engine import generate_summary

app = Flask(__name__)
@app.route("/ping")
def ping():
    return "Pong"

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    transcript = ""
    if request.method == "POST":
        transcript = request.form.get("transcript", "")
        summary = generate_summary(transcript)

    return render_template("index.html", summary=summary, transcript=transcript)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

