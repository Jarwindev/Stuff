import pyautogui 
for x in range(0, 100, 10):
    for y in range(0, 100, 10):
        print(pyautogui.pixel(x, y))  
# This code will print the RGB color values of pixels in a grid from (0, 0) to (990, 990) with a step of 10.
# You can adjust the range and step size as needed.
