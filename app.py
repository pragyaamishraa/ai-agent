import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Agent is running"

@app.route('/ask')
def ask():
    question = request.args.get("question")

    response = f"You asked: {question}. This is a simple response."

    return jsonify({"response": response})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
