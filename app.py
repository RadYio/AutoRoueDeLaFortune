from flask import Flask

import requests
import datetime

from dotenv import load_dotenv
import os

load_dotenv()
PHP_SESSION_ID = os.getenv("PHPSESSID")

app = Flask(__name__)


LOG_FILE = "logs.txt"


def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

@app.route('/')
def home():
    return f"<h1>Projet d'automatisation de la roue de la fortune !</h1>"

@app.route('/check')
def check_logs():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.read().replace("\n", "<br>")
        return f"<h1>Logs du bot :</h1><p>{logs}</p>"
    except FileNotFoundError:
        return "<h1>Aucun log pour le moment.</h1>"

@app.route('/aucasou')
def contact():
    return f"<h1>Page de au cas ou => {PHP_SESSION_ID}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
