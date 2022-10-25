import json
from enum import *
from json import *


class CustomEnum(Enum):
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other

        if type(other) is type(self):
            return super().__eq__(other)

        return False


class Feature:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name', None)
        self._tags: list = kwargs.get('tags', [])
        self._shortdesc: str = kwargs.get('shortdesc', None)
        self._longdesc: str = kwargs.get('longdesc', None)

        self.shortgrammar = kwargs.get('shortgrammar', kwargs.get('grammar', 'a'))
        self.longgrammar = kwargs.get('longgrammar', kwargs.get('grammar', 'a'))

    def checkfortag(self, tag: str) -> bool:
        if tag.lower() in self._tags:
            return True
        else:
            return False

    class Desc(CustomEnum):
        LONG = 'longdesc'
        SHORT = 'shortdesc'

    def gettags(self) -> list:
        return self._tags

    def getdesc(self, desctype: Desc = Desc.SHORT) -> str:
        if desctype == Feature.Desc.LONG:
            return self._longdesc
        elif desctype == Feature.Desc.SHORT:
            return self._shortdesc
        else:
            return self.name


class Creature(Feature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        stats: dict = kwargs.get('stats', {})
        self.vit = stats.get('vit') if stats.get('vit') is not None else 1
        self.str = stats.get('str') if stats.get('str') is not None else 1
        self.dex = stats.get('dex') if stats.get('dex') is not None else 1
        self.end = stats.get('end') if stats.get('end') is not None else 1
        self.run = stats.get('run') if stats.get('run') is not None else 1

    def __str__(self):
        return '<class Creature>'


class Item(Feature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Key(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.door: Door = kwargs.get('door', None)


class Object(Feature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Door(Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.locked: bool = kwargs.get('locked', False)
        self.exit: Room = kwargs.get('room', None)
        self.exitcoords: list[int] = kwargs.get('exitcoords', None)


class Room(Feature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._items: list = kwargs.get('items', [])
        self._objects: list = kwargs.get('objects', [])
        self._creatures: list = kwargs.get('creatures', [])

    def getfeatures(self) -> list:
        return self._items + self._objects + self._creatures

    def getfeatures_sorted(self) -> list:
        out = self.getfeatures()
        out.sort()
        return out

    def getfeatures_categorized(self) -> dict:
        return {'creatures': self._creatures, 'items': self._items, 'objects': self._objects}

    def getitems(self) -> list:
        return self._items

    def getitems_sorted(self) -> list:
        out = self.getitems()
        out.sort()
        return out

    def getobjects(self) -> list:
        return self._objects

    def getobjects_sorted(self) -> list:
        out = self.getobjects()
        out.sort()
        return out

    def getcreatures(self) -> list:
        return self._creatures

    def getcreatures_sorted(self) -> list:
        out = self.getcreatures()
        out.sort()
        return out

    def find(self, item: str) -> [Feature, None]:
        item = item.lower()

        for i in self._items:
            i: Item
            if i.name.lower() == item:
                return i

        for o in self._objects:
            o: Object
            if o.name.lower() == item:
                return o

        for c in self._creatures:
            c: Creature
            if c.name.lower() == item:
                return c

        for i in self._items:
            i: Item
            if i.checkfortag(item):
                return i

        for o in self._objects:
            o: Object
            if o.checkfortag(item):
                return o

        for c in self._creatures:
            c: Creature
            if c.checkfortag(item):
                return c

        return None

    def __len__(self):
        return len(self._items) + len(self._objects) + len(self._creatures)


class Cell:
    def __init__(self, room: Room, **kwargs):
        self.Room = room
        self.direction = kwargs.get('direction', {'n': None, 's': None, 'e': None, 'w': None})


class Floor:
    def __init__(self, items: list):
        self._items = items

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value


class World:
    def __init__(self, floors: list):
        self._items = floors

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value


from structures import Rooms


class Player(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.location: dict = {'x': 0, 'y': 0, 'z': 0, 'room': Rooms.Test.value}


class Command:
    def __init__(self, rawcmd: dict):
        self.rawcmd = rawcmd
