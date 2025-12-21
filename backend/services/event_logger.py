from datetime import datetime, UTC
from storage.database import log_event

def log_focus_event(window, focused, reason):
    utc_time_aware = datetime.now(UTC)
    timestamp = utc_time_aware.isoformat()
    log_event(timestamp, window, focused, reason)