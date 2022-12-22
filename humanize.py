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
