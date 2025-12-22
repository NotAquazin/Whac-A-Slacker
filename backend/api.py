from storage.database import conn

class API:
    def get_recent_events(self):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM events ORDER BY timestamp DESC LIMIT 5"
        )
        return cursor.fetchall()