Awesome! 🎉 Now that your project is published on GitHub, here’s a complete and clean **`README.md`** you can paste into your repo:

---

````markdown
 🧠 AI Assistant – Flask Web App

A simple AI-powered assistant built using Flask and Groq's LLM API.  
This assistant can:
- ✅ Answer factual questions
- 📝 Summarize input text
- 🎨 Generate creative content like stories or poems
- 👍 Accept user feedback to improve prompts

---

🚀 Features

- Clean and user-friendly web interface
- Supports 3 core functionalities:
  - Answer a Question
  - Summarize Text
  - Generate Creative Content
- Response formatted properly (story/poem style)
- Feedback buttons for user input (👍/👎)
- Stores feedback in `feedback_log.txt`



🛠️ Tech Stack

- Python 3
- Flask
- [Groq API](https://console.groq.com/)
- HTML/CSS (Jinja2 templating)

---

 ⚙️ Setup Instructions
### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-assistant-flask.git
cd ai-assistant-flask
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

> Don’t share your API key. Keep `.env` in `.gitignore`.

### 4. Run the App

```bash
python main.py
```

The app will run at `http://localhost:5000`

---

## 🌐 Live Demo

> \[Add your Render link here once deployed]

---

## 📁 File Structure

```
ai-assistant-flask/
├── main.py
├── templates/
│   └── index.html
├── feedback_log.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

✨ Credits

* Built by Hrishita(https://github.com/Hrishita007)
* Powered by [Groq API](https://console.groq.com/)
