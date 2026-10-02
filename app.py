from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "comment" not in data:
        return jsonify({"error": "No text received"}), 400

    text = data["comment"].lower()

    toxic_words = [
        "stupid",
        "idiot",
        "garbage",
        "worthless",
        "hate"
    ]

    spam_words = [
        "buy",
        "crypto",
        "http",
        "www",
        "deal"
    ]

    # Toxic content
    if any(word in text for word in toxic_words):
        return jsonify({
            "probability": 0.92,
            "action": "BLOCKED"
        })

    # Spam content
    if any(word in text for word in spam_words):
        return jsonify({
            "probability": 0.38,
            "action": "FLAGGED"
        })

    # Safe content
    return jsonify({
        "probability": 0.05,
        "action": "APPROVED"
    })


if __name__ == "__main__":
    app.run(debug=True)