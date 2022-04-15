from enum import *
from classes import *


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


class CustomEnum(Enum):
    def __getattribute__(self, item):
        attr = super().__getattribute__(item)
        return attr


class Items(CustomEnum):
    Nothing = Item(
        name='None',
        tags=['nothing'],
        shortdesc='nothing',
        longdesc='whole lot of nothing',
        grammar='a'
    )


class Objects(CustomEnum):
    Nothing = Object(
        name='None',
        tags=['nothing'],
        shortdesc='nothing',
        longdesc='whole lot of nothing',
        grammar='a'
    )


class Creatures(CustomEnum):
    Nothing = Object(
        name='None',
        tags=['nothing'],
        shortdesc='nothing',
        longdesc='whole lot of nothing',
        grammar='a'
    )


class Rooms(CustomEnum):
    Nothing = Object(
        name='None',
        tags=['nothing'],
        shortdesc='nothing',
        longdesc='whole lot of nothing',
        grammar='a',
        items=[
            Items.Nothing,
        ],
        objects=[
            Objects.Nothing,
        ],
        creatures=[
            Creatures.Nothing
        ]
    )
