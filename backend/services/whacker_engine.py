PRODUCTIVE_KEYWORDS = ["Whac-A-Slacker", "Visual Studio Code", "PyCharm", "Terminal", "YouTube Music"]
#Note: Temporary; keywords would be loaded from user settings.
#      Keywords can either be the app or their specific tab (like a google tab)

def evaluate_focus(window_title: str):
    for keyword in PRODUCTIVE_KEYWORDS:
        if keyword.lower() in window_title.lower():
            return True, "productive_app"
    return False, "non_productive_app"