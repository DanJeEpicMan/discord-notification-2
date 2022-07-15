import pyautogui
import os
os.system('color 84')
os.system('title Discord 2')

for _ in range(7):
    pyautogui.hotkey("ctrl", "shift", "-")

import win32gui
import win32con
hwnd = win32gui.GetForegroundWindow()#          xpos ypos width hight importance
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,500,500,0)
os.system('cls')


'''
# 90% Transparency
for _ in range(1):
    pyautogui.hotkey("ctrl", "shift", "-")

# 80% Transparency
for _ in range(2):
    pyautogui.hotkey("ctrl", "shift", "-")

# 70% Transparency
for _ in range(3):
    pyautogui.hotkey("ctrl", "shift", "-")

# 60% Transparency
for _ in range(4):
    pyautogui.hotkey("ctrl", "shift", "-")
'''