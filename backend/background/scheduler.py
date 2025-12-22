import time
from services.window_tracker import get_foreground_window_title
from services.whacker_engine import evaluate_focus
from services.event_logger import log_focus_event

def focus_loop():
    previous_window = None
    while True:
        current_window = get_foreground_window_title()
        if current_window != previous_window:
            focused, reason = evaluate_focus(current_window)
            log_focus_event(current_window, focused, reason)
            print(current_window)
            print(focused)
            print(reason)
            
        previous_window = get_foreground_window_title()
        time.sleep(1)

def start_background_tasks():
    import threading
    threading.Thread(target=focus_loop, daemon=True).start()