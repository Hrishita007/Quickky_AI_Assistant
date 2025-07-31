from flask import Flask, render_template, request, redirect, url_for, flash
import os
import openai

app = Flask(__name__)
app.secret_key = "secret"  # Needed for flash messages

# Set Groq API key and base URL (for old SDK)
openai.api_key = os.environ.get("GROQ_API_KEY", "")
openai.api_base = "https://api.groq.com/openai/v1"  # note: no trailing slash

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        task = request.form.get("task")
        user_input = request.form.get("user_input")

        if task == "question":
            prompt = f"Answer this question clearly: {user_input}"
        elif task == "summary":
            prompt = f"Summarize the following text: {user_input}"
        elif task == "creative":
            prompt = f"Write a story or poem about: {user_input}"
        else:
            prompt = ""

        if prompt:
            try:
                response = openai.ChatCompletion.create(
                    model="llama3-8b-8192",  # or mixtral
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=400
                )
                result = response.choices[0].message["content"].strip()
            except Exception as e:
                result = f"Error: {e}"

    return render_template("index.html", result=result)

@app.route("/feedback", methods=["POST"])
def feedback():
    user_feedback = request.form.get("feedback")
    print("User Feedback:", user_feedback)  # Optional: console log

    with open("feedback_log.txt", "a") as f:
        f.write(f"{user_feedback}\n")

    flash("Thanks for your feedback!", "info")
    return redirect(url_for("index"))
