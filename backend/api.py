from storage.database import conn, get_last_event

class API:
    def get_recent_events(self):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM events ORDER BY timestamp DESC LIMIT 5"
        )
        return cursor.fetchall()
    
    def get_focus_status(self):
        event = get_last_event()
        if not event:
            return {
                "isFocused": True,
                "windowTitle": "",
                "reason": "no event data"
            }

        return {
            "isFocused": bool(event["is_focused"]),
            "windowTitle": event["window_title"],
            "reason": event["reason"]
        }    