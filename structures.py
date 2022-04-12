from enum import *


class TextSpeed(Enum):
    INSTANT = 0.0
    HYPER = 0.01
    FAST = 0.04
    NORMAL = 0.08
    SLOW = 0.12
    SNAIL = 0.3

    @staticmethod
    def getvalfromstr(key: str):
        for k in TextSpeed.__members__:
            if key == k:
                return TextSpeed.__members__[k]
        return None
