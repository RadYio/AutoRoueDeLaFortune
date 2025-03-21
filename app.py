# Import(s)

from flask import Flask, request

import datetime

from dotenv import load_dotenv
import os

from bot_requests import trigger_daily_roue, get_delay_before_next_wheel
from gestion_db import init_db, insert_or_update_account_info, get_account_info

# Fin Import(s)
# Constante(s)
LOG_FILE = "logs.txt" # Nom du fichier de logs

# Fin Constante(s)
# Fonction(s)
def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

# Fin Fonction(s)
# Début du programme

app = Flask(__name__) 

# Avant tout on initialise la base de données
log_message("Initialisation de la base de données...")
init_db()

load_dotenv()
PHP_SESSION_ID = os.getenv("PHPSESSID")

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

@app.route('/send_post')
def send_post():
    try:
        status, response_text = trigger_daily_roue(PHP_SESSION_ID)
        log_message(f"POST vers minestrator.com - Status: {status} - Réponse: {response_text}")
        return "<h1>Requête POST envoyée et logguée !</h1>"
    except Exception as e:
        log_message(f"Erreur lors de l'envoi du POST : {e}")
        return f"<h1>Erreur : {e}</h1>"

@app.route('/next_roue')
def next_roue():
    try:
        php_session_id = request.args.get('id')  # On récupère l'ID dans les paramètres de l'URL
        if not php_session_id:
            return "<h1>Erreur : aucun ID fourni dans la requête.</h1>", 400

        status, response_text = get_delay_before_next_wheel(php_session_id)
        log_message(f"POST vers minestrator.com - Status: {status} - Réponse: {response_text}")
        return "<h1>Requête POST envoyée et logguée !</h1>"
    except Exception as e:
        log_message(f"Erreur lors de l'envoi du POST : {e}")
        return f"<h1>Erreur : {e}</h1>"

@app.route('/aucasou')
def contact():
    return f"<h1>Page de au cas ou => {PHP_SESSION_ID}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
