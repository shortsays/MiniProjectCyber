import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../phishing.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            source TEXT,
            url TEXT,
            confidence REAL
        )
    """)

    conn.commit()
    conn.close()


def insert_log(time, source, url, confidence):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (time, source, url, confidence) VALUES (?, ?, ?, ?)",
        (time, source, url, confidence)
    )

    conn.commit()
    conn.close()


def fetch_logs(limit=100):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT ?", (limit,))
    data = cursor.fetchall()

    conn.close()
    return data