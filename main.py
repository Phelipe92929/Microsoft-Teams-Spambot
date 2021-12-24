import pyautogui
import time
import keyboard
import win32api, win32con

spam = input("What do you want to spam? ")
spam_amount = input("How many times would you like to spam? ")
time.sleep(1)
print(f"Spamming {spam} {spam_amount} times.")
time.sleep(2)
print("Do not click or type anything after you have switched to teams.")
time.sleep(2)
print("Manually move cursor to the top-left corner of the screen if you want to stop spamming.")
time.sleep(2)
print("You have 10 Seconds to switch to Teams.")
time.sleep(10)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

try:
    for i in range(int(spam_amount)):
        click(940, 952)
        time.sleep(0.3)
        pyautogui.write(spam)
        time.sleep(0.3)
        pyautogui.press("tab")
        click(1777, 997)
        time.sleep(0.3)
except pyautogui.FailSafeException:
    print("\n Stopped spamming")