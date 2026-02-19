from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os, requests

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    topic = request.args.get('topic', '').strip()
    sort = request.args.get('sort', 'publishedAt')

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    url = (
        "https://newsapi.org/v2/everything"
        f"?q={requests.utils.quote(topic)}"
        f"&sortBy={sort}"
        f"&apiKey={API_KEY}"
        "&pageSize=20"
    )

    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()

        if data.get("status") != "ok":
            return jsonify({"error": data.get("message", "Failed to fetch")}), 500

        articles = data.get("articles", [])[:15]
        result = [
            {
                "title": a.get("title"),
                "url": a.get("url"),
                "source": a.get("source", {}).get("name")
            }
            for a in articles
        ]

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)











# python -u "d:\pythonprojectsand all\OSMOD\NEWSAPP\NEWSAPPMINI_V2\app.py"