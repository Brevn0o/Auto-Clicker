import random
import threading
import time

import pyautogui as pg
from typing import Literal


class Clicker:

    def __init__(self):
        self.clicking = False
        self.click_types = {
            'single': 1,
            'double': 2,
            'triple': 3
        }

    def click(self, x: int = None, y: int = None, duration: float = 0, button: str = 'left',
              click_type: str = 'single', anti_detect: int = 0):
        if x is not None and y is not None:
            x = x + random.randrange(-anti_detect, anti_detect)
            y = y + random.randrange(-anti_detect, anti_detect)
        button = pg._normalizeButton(button)
        x, y = pg._normalizeXYArgs(x, y)
        pg._mouseMoveDrag("move", x, y, 0, 0, 0)
        for _ in range(self.click_types[click_type]):
            if duration == 0:
                pg._pyautogui_win._click(x=x, y=y, button=button)
            else:
                pg._pyautogui_win._mouseDown(x=x, y=y, button=button)
                time.sleep(duration)
                pg._pyautogui_win._mouseUp(x=x, y=y, button=button)

    def start(self, interval: int, times: int = -1, duration: float = 0, button: str = 'left',
              click_type: str = 'single', x: int = None, y: int = None, anti_detect: int = 0,
              interval_randomization: int = 0):
        self.clicking = True
        count = 0
        while self.clicking:
            self.click(x, y, duration, button, click_type, anti_detect)
            randomized_interval = 0
            if interval_randomization > 0:
                randomized_interval = random.randrange(-interval_randomization, interval_randomization)
            if interval + randomized_interval < 0:
                randomized_interval = 0
            time.sleep(interval + randomized_interval / 1000)
            if count >= times != -1:
                self.clicking = False
                break
            count += 1

    def stop_clicking(self):
        self.clicking = False


# time.sleep(2)
# clicker = Clicker()
# threading.Thread(target=clicker.stop_clicking,).start()
# clicker.start_clicking(.01, 100, 0, 'left', anti_detect=10)
