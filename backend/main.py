import webview
from api import API
from background.scheduler import start_background_tasks
from storage.database import init_db
from pathlib import Path

def start_app():
    init_db()

    web_dir = Path(__file__).resolve().parent.parent/"web"
    index_file = web_dir/"index.html"

    window = webview.create_window(
        "Whac-A-Slacker",
        index_file.as_uri(),
        js_api=API()
    )

    webview.start()

if __name__ == "__main__":
    start_app()