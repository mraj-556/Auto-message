import pyautogui as pg
import time

txt = ['hi','hello','are you fine']
for i in range(50):
    for j in txt:
        pg.write(j)
        pg.press('Enter')
        time.sleep(1)
