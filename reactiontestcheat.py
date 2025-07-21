import pyautogui


while True:
    if pyautogui.pixelMatchesColor(200, 300, (75, 219, 106)):
        pyautogui.click(200, 300)
        print("Clicked on the pixel at (200, 300) with color (75, 219, 106)")
        break

