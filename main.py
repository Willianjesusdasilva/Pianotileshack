from PIL import ImageGrab
import pyautogui

while True:
    img = ImageGrab.grab().load()
    if img[297, 696] == (0, 0, 0):
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
    if img[369, 696] == (0, 0, 0):
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')
    if img[449, 696] == (0, 0, 0):
        pyautogui.keyDown('d')
        pyautogui.keyUp('d')
    if img[519, 696] == (0, 0, 0):
        pyautogui.keyDown('f')
        pyautogui.keyUp('f')