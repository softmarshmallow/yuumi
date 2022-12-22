import osmac
import time
import threading
import humanize
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
    skill_priority = ['r', 'e', 'q', 'w']
    for skill in skill_priority:
        skill_up(skill)
        time.sleep(0.5)
    skill_up('w')  # 4


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
    # right click
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

    def __init__(self, interval=20.0):
        self.interval = interval

    def start(self):
        threading.Timer(self.interval, self.update).start()

    def update(self):
        print('heal queued by HealManager#update')
        skill_up('e')
        start_skill('e')
        self.start()


if __name__ == '__main__':
    time.sleep(3)
    SkillUpManager().start()
    HealManager().start()
