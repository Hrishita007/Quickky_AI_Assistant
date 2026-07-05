from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
app.secret_key = "secret"

# Load Groq API key
api_key = os.environ.get("GROQ_API_KEY")
client = None
if api_key:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1/"
    )
else:
    app.logger.warning("GROQ_API_KEY is not set. Add it to .env or environment variables.")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    supported_models = [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b",
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile"
    ]
    model = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")

    if request.method == "POST":
        task = request.form.get("task")
        user_input = request.form.get("user_input")
        model = request.form.get("model", model)
        if model not in supported_models:
            model = "openai/gpt-oss-120b"

        if task == "question":
            prompt = f"Answer this question clearly: {user_input}"
        elif task == "summary":
            prompt = f"Summarize the following text: {user_input}"
        elif task == "creative":
            prompt = f"Write a story or poem about: {user_input}"
        else:
            prompt = ""

        if prompt:
            if client is None:
                result = "Error: GROQ_API_KEY is not configured. Set it in .env or environment variables."
            else:
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=400
                    )
                    result = response.choices[0].message.content.strip()
                except Exception as e:
                    result = f"Error: {e}"

    return render_template("index.html", result=result, model=model)

@app.route("/feedback", methods=["POST"])
def feedback():
    user_feedback = request.form.get("feedback")
    with open("feedback_log.txt", "a") as f:
        f.write(f"{user_feedback}\n")
    flash("Thanks for your feedback!", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
