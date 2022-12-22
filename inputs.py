import pyautogui
PRIMARY = pyautogui.PRIMARY


class InputManager:

    def __init__(self, before_input=None):
        self.before_input = before_input

    def __input_if_valid(self, input):
        if self.before_input is None:
            return
        else:
            if self.before_input():
                input()

    def keyDown(self, key):
        self.__input_if_valid(lambda: pyautogui.keyDown(key))

    def keyUp(self, key):
        self.__input_if_valid(lambda: pyautogui.keyUp(key))

    def press(self, key, presses=1, interval=0.0):
        self.__input_if_valid(lambda: pyautogui.press(
            key, presses=presses, interval=interval))

    def click(self, x=None, y=None, clicks=1, interval=0.0, button=PRIMARY):
        self.__input_if_valid(lambda: pyautogui.click(
            x, y, clicks=clicks, interval=interval, button=button))
