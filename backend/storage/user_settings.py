import json
from pathlib import Path

SETTINGS_FILE = Path("data/settings.json")

DEFAULT_SETTINGS = {
    "productive_apps": [],
    "productive_keywords": [],
    "non_productive_apps": [],
    "non_productive_keywords": []
}

def load_settings():
    if not SETTINGS_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
    return json.loads(SETTINGS_FILE.read_text())

def save_settings(settings: dict):
    SETTINGS_FILE.parent.mkdir(exist_ok=True)
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2))