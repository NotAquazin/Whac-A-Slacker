from storage.database import conn, get_last_event
from background.scheduler import pause_background_tasks, resume_background_tasks, stop_background_tasks, start_background_tasks

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
    
    def start_tracking(self):
        start_background_tasks()


    def pause_tracking(self):
        pause_background_tasks()
    

    def resume_tracking(self):
        resume_background_tasks()


    def stop_tracking(self):
        stop_background_tasks()