import win32gui
from services.whacker_engine import evaluate_focus

def getForegroundWindowTitle():
    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except Exception as e:
        return str(e)

print(getForegroundWindowTitle())
print(evaluate_focus(getForegroundWindowTitle()))
print(win32gui.GetActiveWindow())