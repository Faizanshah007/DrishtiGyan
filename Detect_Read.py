import win32gui

import time

while True:
    if (win32gui.GetWindowText(win32gui.GetForegroundWindow()).find(".pdf") != -1):
        print("Good")
    else:
      print("bad")
    time.sleep(0.1)
