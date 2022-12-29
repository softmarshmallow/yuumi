import osmac
import random
import time
import threading
import humanize
import chat
import pyautogui
from inputs import InputManager
# skull data


# if the dev mode is enabled, the inputs won't be triggered unless the game is focused
DEV_MODE = True


def is_game_focused():
    return osmac.leage_of_legends_game_client_focused()


def allow_input():
    if DEV_MODE:
        return is_game_focused()
    return True


input = InputManager(before_input=allow_input)


def skill_up(type):
    # input: ctrl + type
    input.keyDown('ctrl')
    time.sleep(humanize.seconds(0.1))
    input.press(type)
    time.sleep(humanize.seconds(0.1))
    input.keyUp('ctrl')


def skill_up_all():
    skill_priority = ['r', 'e', 'w', 'q']
    for skill in skill_priority:
        skill_up(skill)
        time.sleep(1)


def skill_q_up():
    skill_up('q')


def skill_w_up():
    skill_up('w')


def skill_e_up():
    skill_up('e')


def skill_r_up():
    skill_up('r')


def start_skill(skill):
    input.press(skill)


def move_commit(pos):
    # move to pos
    input.moveTo(pos[0], pos[1], duration=humanize.seconds(0.3))
    # randomize times to click between 1 and 3 times
    for i in range(random.randint(1, 3)):
        # right click
        time.sleep(humanize.seconds(0.1))
        input.click(pos[0], pos[1], button='right')


class SkillUpManager:
    """
    skill up manager

    trigger skill up all (without knowledge of current level and availability) every n seconds
    """

    def __init__(self, interval=45.0):
        self.interval = interval

    def start(self):
        threading.Timer(self.interval, self.update).start()

    def update(self):
        print('skill up queued by SkillUpManager#update')
        skill_up_all()
        self.start()


class HealManager:
    """
    heal manager

    trigger heal every n seconds
    """

    def __init__(self, interval=13.0):
        self.interval = interval

    def start(self):
        sec = humanize.seconds(self.interval)
        threading.Timer(sec, self.update).start()

    def update(self):
        print('heal queued by HealManager#update')
        skill_up('e')
        start_skill('e')
        self.start()


class ChatManager:
    """
    chat manager

    trigger chat every n seconds
    """

    def __init__(self, interval=120.0):
        self.interval = interval
        self.chat_client = chat.ChatClient(input)

    def start(self):
        threading.Timer(self.interval, self.update).start()

    def update(self):
        print('chat queued by ChatManager#update')
        # pick random script from chat.hard_scripts
        self.chat_client.chat(random.choice(chat.hard_scripts))
        self.start()


class MovementManager:
    """
    movement manager

    trigger movement every n seconds
    """

    def __init__(self, interval=2.0):
        self.center = pyautogui.position()
        self.interval = interval
        self.unit = 100
        self.movements = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]

    def start(self):
        sec = humanize.seconds(self.interval)
        threading.Timer(sec, self.update).start()

    def update(self):
        # pick random movement from self.movements
        relpos = (random.choice(self.movements))
        rx = humanize.pixels(self.unit)
        ry = humanize.pixels(self.unit)
        relpos = (relpos[0] * rx, relpos[1] * ry)

        pos = (self.center[0] + relpos[0], self.center[1] + relpos[1])

        move_commit(pos)
        self.start()


if __name__ == '__main__':
    SkillUpManager().start()
    HealManager().start()

    #
    time.sleep(90)
    MovementManager().start()

    #
    time.sleep(3)
    ChatManager().start()
