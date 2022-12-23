import time
import humanize
from inputs import InputManager


class ChatClient:
    def __init__(self, input: InputManager):
        self.input = input

    def _send(self, text):
        # enter chat (Enter key)
        self.input.press('enter')
        # type text
        self.input.typewrite(text, interval=0.05)
        # send chat (Enter key)
        self.input.press('enter')

    def chat(self, texts):
        if isinstance(texts, str):
            texts = [texts]

        for text in texts:
            self._send(text)
            time.sleep(humanize.seconds(1.5))


hard_scripts = [
    ["z", "ㅋㅋ"],
    ["dk.."],
    ["ㄱㅊㄱㅊㄱ"],
    ["ㅠ,"]
]
