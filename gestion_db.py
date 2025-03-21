import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = 1")  # Aucune idée de si necessaire
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        php_session_id varchar(255),
        pseudo varchar(255),
        mail varchar(255),
        mot_de_passe varchar(255)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        log TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    # Save
    conn.commit()
    conn.close()


def insert_or_update_account_info(php_session_id: str, pseudo: str, solde: int, delai: str):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()


    cursor.execute('''
    INSERT INTO comptes (php_session_id, pseudo, solde, delai)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(php_session_id) DO UPDATE SET
        pseudo=excluded.pseudo,
        solde=excluded.solde,
        delai=excluded.delai
    ''', (php_session_id, pseudo, solde, delai))

    # Save
    conn.commit()
    conn.close()

def insert_log(user_id: int, log: str):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO logs (user_id, log)
    VALUES (?, ?)
    ''', (user_id, log))

    # Save
    conn.commit()
    conn.close()


def get_account_info(php_session_id: str):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT pseudo, solde, delai
    FROM comptes
    WHERE php_session_id = ?
    ''', (php_session_id,))

    result = cursor.fetchone()

    conn.close()
    return result