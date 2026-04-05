import os
import requests
from flask import Flask

FLASK_PORT = os.environ.get("SERVER1_PORT")
SERVER2_URL = os.environ.get("SERVER2_URL")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")

app = Flask(__name__)
webhook_session = requests.session()
webhook_session.headers.update({"webhook-signature": WEBHOOK_SECRET})


@app.route("/send-message", methods=["POST"])
def send_message():
    print(WEBHOOK_SECRET)
    response = webhook_session.post(f"{SERVER2_URL}/webhook", json={"message": "Hello from server 1!"})
    if response.status_code == 200:
        return "message sent", 200
    else:
        return "failed to send message", response.status_code

if __name__ == "__main__":
    app.run(port=FLASK_PORT)
