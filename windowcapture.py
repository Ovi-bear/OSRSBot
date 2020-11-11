import cv2 as cv
import numpy as np
from PIL import ImageGrab
import win32gui



class WindowCapture:
    hwnd = None
    position = None

    def __init__(self,window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        self.position = win32gui.GetWindowRect(self.hwnd)
        win32gui.SetForegroundWindow(self.hwnd)

    def capture_screen(self):
        screenshot = ImageGrab.grab(self.position)
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        return screenshot






