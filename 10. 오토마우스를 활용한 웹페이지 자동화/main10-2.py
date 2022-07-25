import pyautogui
import time
import pyperclip


pyautogui.moveTo(-991, 215, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("seoul weather")
pyautogui.hotkey("command","v")
time.sleep(1)

pyautogui.write(["enter"])
time.sleep(3)

#오토마우스로 서울 날씨 검색하는 코드