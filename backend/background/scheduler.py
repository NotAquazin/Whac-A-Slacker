import time
import threading
from services.window_tracker import get_foreground_window_title
from services.whacker_engine import evaluate_focus
from services.event_logger import log_focus_event


def focus_loop(stop_event, pause_event):
    previous_window = None
    while not stop_event.is_set():

        pause_event.wait()

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
    stop_event.clear()
    pause_event.set()
    threading.Thread(
        target=focus_loop,
        daemon=True,
        args=(stop_event, pause_event)
    ).start()


def stop_background_tasks():
    stop_event.set()


def pause_background_tasks():
    pause_event.clear()


def resume_background_tasks():
    pause_event.set()


stop_event = threading.Event()
pause_event = threading.Event()
pause_event.set()
