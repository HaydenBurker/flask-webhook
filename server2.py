import os
from flask import Flask

FLASK_PORT = os.environ.get("SERVER2_PORT")
app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=FLASK_PORT)
