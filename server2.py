import os
from flask import Flask, request

FLASK_PORT = os.environ.get("SERVER2_PORT")
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    print("webhook event: ", request.get_json())
    return "success", 200

if __name__ == "__main__":
    app.run(port=FLASK_PORT)
