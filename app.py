from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

HF_API_KEY = os.getenv("HF_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/category/<name>")
def category(name):
   
    if name == "ai":
        url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={API_KEY}"
    
    elif name == "world":
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    else:
        url = f"https://newsapi.org/v2/top-headlines?category={name}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    articles = articles[:5]

    return render_template("news.html", articles=articles, category=name)


def summarize_text(text):
    url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    payload = {
        "inputs": text
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    print(result)

    if isinstance(result, list):
        return result[0].get("summary_text", "No summary found")
    
    elif "error" in result:
        return f"API Error: {result['error']}"
    
    return "Unexpected response"


@app.route("/summarize")
def summarize():
    text = request.args.get("text")
    category = request.args.get("category")

    
    if text:
        summary = summarize_text(text)
    else:
        summary = "No text provided"

    
    if category == "ai":
        url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={API_KEY}"
    
    elif category == "world":
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    else:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    articles = articles[:5]

    return render_template(
        "news.html",
        articles=articles,
        category=category,
        summary=summary
    )


@app.route("/api/summarize")
def api_summarize():
    text = request.args.get("text")

    if text:
        summary = summarize_text(text)
    else:
        summary = "No text provided"

    return {"summary": summary}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)