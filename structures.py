from classes import *


class TextSpeed(CustomEnum):
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


class Items(CustomEnum):
    Nothing = Item(**{
        'name': 'none',
        'tags': ['nothing'],
        'shortdesc': 'nothing',
        'longdesc': 'whole lot of nothing',
        'grammar': 'a'
    })


class Objects(CustomEnum):
    Nothing = Object(**{
        'name': 'none',
        'tags': ['nothing'],
        'shortdesc': 'nothing',
        'longdesc': 'whole lot of nothing',
        'grammar': 'a'
    }),
    PrisonSkeleton = Object(**{
        'name': 'skeleton',
        'tags': ['skelly', 'skeleton', 'body', 'corpse', 'prisoner', 'dead', 'guy', 'person'],
        'shortdesc': 'old skeleton up against the wall',
        'longdesc': 'bleached, old skeleton of the last poor sod to be thrown in here',
        'shortgrammar': 'an',
        'longgrammar': 'a'
    })


class Creatures(CustomEnum):
    Nothing = Object(**{
        'name': 'none',
        'tags': ['nothing'],
        'shortdesc': 'nothing',
        'longdesc': 'whole lot of nothing',
        'grammar': 'a'
    })
    KeyRat = Creature(**{
        'name': 'none',
        'tags': ['nothing'],
        'shortdesc': 'nothing',
        'longdesc': 'whole lot of nothing',
        'grammar': 'a',
        'stats': {
            'vit': 0,
            'str': 0,
            'dex': 0,
            'end': 0,
            'run': 0
        }
    }),


class Rooms(CustomEnum):
    Nothing = Room(**{
        'name': 'none',
        'tags': ['nothing'],
        'shortdesc': 'nothing',
        'longdesc': 'whole lot of nothing',
        'longgrammar': 'a',
        'shortgrammar': 'abuncha',
        'items': [],
        'objects': [],
        'creatures': []
    })
    Test = Room(**{
        'name': 'none',
        'tags': ['nothing'],
        'shortdesc': 'nothing',
        'longdesc': 'whole lot of nothing',
        'longgrammar': 'a',
        'shortgrammar': 'abuncha',
        'items': [],
        'objects': [Objects.PrisonSkeleton.value, Objects.PrisonSkeleton.value, Objects.PrisonSkeleton.value, Objects.PrisonSkeleton.value, Objects.PrisonSkeleton.value],
        'creatures': []
    })
    StartCell = Room(**{
        'name': 'cell',
        'tags': ['cell', 'room', 'prison'],
        'shortdesc': 'cramped, moldy cell',
        'longdesc': 'tiny, cramped cell full of mold and mildew',
        'grammar': 'a',
        'items': [],
        'objects': [Objects.PrisonSkeleton.value],
        'creatures': []
    })
