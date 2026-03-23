# 🧠 AI News Assistant

🚀 Live Demo: https://ai-news-app-4e8x.onrender.com

An AI-powered full-stack web application that fetches real-time news and generates concise summaries using NLP models.

---

## 🚀 Features

- 📰 Fetch real-time news using NewsAPI  
- 🧠 AI-powered summarization using Hugging Face  
- ⚡ Instant summary (no page reload using JavaScript)  
- 🌍 Categories: Technology, AI, World  
- 🎯 Clean UI with responsive design  
- 🛡️ Secure API handling using environment variables  

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **APIs:** NewsAPI
- **AI Model:** facebook/bart-large-cnn (Hugging Face)
- **Deployment:** Render

---

## ⚙️ How It Works

1. User selects a category (Technology / AI / World)
2. Flask backend fetches news from NewsAPI
3. Articles are displayed dynamically
4. User clicks "Summarize"
5. JavaScript sends request to Flask API (`/api/summarize`)
6. Text is sent to Hugging Face model
7. AI returns summary instantly (no reload)
8. Summary is displayed on screen

---

## 🧠 AI Integration

- Model: `facebook/bart-large-cnn`
- Task: Text Summarization
- Input: Article description/title
- Output: Short meaningful summary

---

## 🔐 Security

- API keys are **NOT stored in code**
- Environment variables used for security:
  - `API_KEY`
  - `HF_API_KEY`
- `.env` file is ignored using `.gitignore`

---

## ⚠️ Challenges Faced

- ❌ NewsAPI doesn't support "AI" category  
  ✔ Solved using keyword-based search  

- ❌ Hugging Face API endpoint change  
  ✔ Updated to new router API  

- ❌ GitHub blocked push due to exposed API keys  
  ✔ Learned and implemented secure environment variables  

- ❌ Flask errors (UnboundLocalError, TypeError)  
  ✔ Fixed variable scope and function logic  

- ❌ Page reload UX issue  
  ✔ Solved using JavaScript Fetch API  

---

## 💡 What I Learned

- Full-stack development (Flask + JS)
- API integration and error handling
- AI model integration (NLP)
- Debugging real-world issues
- Secure coding practices (API protection)
- Deployment using Render

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/Vishwam-Gawande/ai-news-assistant.git
cd ai-news-assistant
pip install -r requirements.txt

▶️ Run Locally
python app.py

Open:

http://127.0.0.1:5000/

🔮 Future Improvements
🔍 Search functionality
💾 Save summaries
👤 User authentication
🌙 Dark mode
📱 Mobile optimization

👨‍💻 Author

Built by [Vishwam Gawande]

⭐ Support

If you like this project, give it a ⭐ on GitHub!
