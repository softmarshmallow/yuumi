import math
import random


def seconds(sec):
    """
    randomize seconds for human-like behavior for automated scheduled inputs
    """
    # scale ranges
    # 0-0.1 (+- 0~0.05)
    # 0.1-1 (+- 0~0.5)
    # 1-5 (+- 0~2.5)
    # 5-10 (+- 0~3)
    # 10 ~ (+- 0~5)
    if sec < 0.1:
        return abs(sec + random.uniform(-0.05, 0.05))
    elif sec < 1:
        return abs(sec + random.uniform(-0.5, 0.5))
    elif sec < 5:
        return abs(sec + random.uniform(-2.5, 2.5))
    elif sec < 10:
        return abs(sec + random.uniform(-3, 3))
    else:
        return abs(sec + random.uniform(-5, 5))


def pixels(size):
    """
    randomize pixels for human-like behavior for automated scheduled inputs
    """
    # scale ranges
    # 0-10 (+- 0~5)
    # 10-100 (+- 0~25)
    # 100-500 (+- 0~100)
    # 500-1000 (+- 0~200)
    # 1000 ~ (+- 0~500)
    if size < 10:
        return abs(size + random.uniform(-5, 5))
    elif size < 100:
        return abs(size + random.uniform(-25, 25))
    elif size < 500:
        return abs(size + random.uniform(-100, 100))
    elif size < 1000:
        return abs(size + random.uniform(-200, 200))
    else:
        return abs(size + random.uniform(-500, 500))
