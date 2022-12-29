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

    def doubleClick(self, x=None, y=None, interval=0.0, button=PRIMARY):
        self.__input_if_valid(lambda: pyautogui.doubleClick(
            x, y, interval=interval, button=button))

    def move(self, x, y, duration=0.0, tween=pyautogui.linear):
        self.__input_if_valid(lambda: pyautogui.move(
            x, y, duration=duration, tween=tween))

    def moveTo(self, x, y, duration=0.0, tween=pyautogui.linear):
        self.__input_if_valid(lambda: pyautogui.moveTo(
            x, y, duration=duration, tween=tween))

    def typewrite(self, message, interval=0.0):
        self.__input_if_valid(lambda: pyautogui.typewrite(
            message, interval=interval))
