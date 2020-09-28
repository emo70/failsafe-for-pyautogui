import pyautogui
import sys
import win32api
import win32con
import time
import datetime

pyautogui.FailSafeException
# When capslock is enabled exit program. If you want to use a keybind use the keyboard module
def caps():
    if win32api.GetKeyState(win32con.VK_CAPITAL) == 1:
        print('exiting...')
        sys.exit()


# Pause the program
def pause():
    while win32api.GetKeyState(win32con.VK_SCROLL) == 1:
        print('paused...')
        time.sleep(0.1)


# Kill the program at given time
def kill():
    now = datetime.datetime.now()
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    second = int(now.strftime("%S"))
    check = datetime.datetime(
        year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    kill = datetime.datetime(
        year=year, month=month, day=day, hour=6, minute=minute, second=second)
    if kill <= check:
        print('End of program.')
        sys.exit()

