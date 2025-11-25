from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("user")
    response = f"Placeholder reply for: {user_msg}"
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(port=7860)
