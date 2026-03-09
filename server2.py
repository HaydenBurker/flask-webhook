import os
from flask import Flask, request, jsonify

FLASK_PORT = os.environ.get("SERVER2_PORT")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get("Webhook-Signature") != WEBHOOK_SECRET:
        return jsonify(success=False), 400
    print("webhook event: ", request.get_json())
    return jsonify(success=True), 200

if __name__ == "__main__":
    app.run(port=FLASK_PORT, debug=True)
