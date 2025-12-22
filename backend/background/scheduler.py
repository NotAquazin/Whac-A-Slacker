import time
from services.window_tracker import get_foreground_window_title
from services.whacker_engine import evaluate_focus
from services.event_logger import log_focus_event

def focus_loop():
    while True:
        window = get_foreground_window_title()
        focused, reason = evaluate_focus(window)
        log_focus_event(window, focused, reason)
        time.sleep(1)

def start_background_tasks():
    import threading
    threading.Thread(target=focus_loop, daemon=True).start()