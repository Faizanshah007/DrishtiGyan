import win32gui

import time

while True:
    
    if ((win32gui.GetWindowText(win32gui.GetForegroundWindow()).find("[~]") != -1)):
        print("Active")
        break
    else:
      print("Un-Active")
