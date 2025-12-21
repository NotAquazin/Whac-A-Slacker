from storage.user_settings import load_settings

def is_productive(window_title: str) -> bool:
    settings = load_settings()

    for keyword in settings["non_productive_keywords"]:
        if keyword.lower() in window_title.lower():
            return False

    for keyword in settings["productive_keywords"]:
        if keyword.lower() in window_title.lower():
            return True

    return True  # default