import sqlite3
import datetime

conn = sqlite3.connect("data/focus.db", check_same_thread=False)

def init_db():
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS focus_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        window_title TEXT,
        is_focused BOOLEAN,
        reason TEXT
    )
    """)
    conn.commit

def log_event(timestamp: datetime, window_title: str, is_focused: bool, reason: str):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO focus_events (timestamp, window_title, is_focused, reason)
    VALUES (?, ?, ?, ?)
    """, (timestamp, window_title, is_focused, reason))
    conn.commit()

def get_last_event():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT is_focused, window_title, reason
        FROM focus_events
        ORDER BY timestamp DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    if not row:
        return None
    return {
        "is_focused": row[0],
        "window_title": row[1],
        "reason": row[2]
        }
    