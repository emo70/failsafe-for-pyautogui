import pyautogui
import sys
import win32api
import win32con


# When capslock is enabled exit program. If you want to use a keybind use the keyboard module
def caps():
    if win32api.GetKeyState(win32con.VK_CAPITAL) == 1:
        print('exiting...')
        sys.exit()


# Set up your bot how you want
autobot = (
    lambda: pyautogui.moveTo(197, 265, duration=1),
    lambda: pyautogui.moveTo(297, 265, duration=1),
    lambda: pyautogui.moveTo(297, 365, duration=1),
    lambda: pyautogui.moveTo(197, 365, duration=1)
)

# Run the program
while True:
    for bot in autobot:
        caps()
        bot()
