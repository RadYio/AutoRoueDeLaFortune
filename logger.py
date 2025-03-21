import datetime
from gestion_db import insert_log


LOG_FILE = "logs.txt" # Nom du fichier de logs


def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")