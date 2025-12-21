PRODUCTIVE_KEYWORDS = ["Visual Studio Code", "PyCharm", "Terminal"]

def evaluate_focus(window_title: str):
    for keyword in PRODUCTIVE_KEYWORDS:
        if keyword.lower() in window_title.lower():
            return True, "productive_app"
    return False, "non_productive_app"