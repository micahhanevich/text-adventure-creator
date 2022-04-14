import enum


class CanBeInWorld:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name', None)
        self._tags: list = kwargs.get('tags', [])
        self._shortdesc: str = kwargs.get('shortdesc', None)
        self._longdesc: str = kwargs.get('longdesc', None)

    def checkfortag(self, tag: str) -> bool:
        if tag in self._tags: return True
        else: return False

    class Desc(enum.Enum):
        LONG = 'longdesc'
        SHORT = 'shortdesc'

    def gettags(self) -> list:
        return self._tags

    def getdesc(self, desctype: Desc) -> str:
        if desctype == CanBeInWorld.Desc.LONG:
            return self._longdesc
        elif desctype == CanBeInWorld.Desc.SHORT:
            return self._shortdesc
        else:
            return self.name


class Creature(CanBeInWorld):
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

    # def __format__(self, format_spec):
    #     return f'<Creature {self.name} | vit: {self.vit} | str: {self.str} | dex: {self.dex} | end: {self.end} | run: {self.run}>'


class Item(CanBeInWorld):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Object(CanBeInWorld):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Room:
    def __init__(self, **kwargs):
        self._id = kwargs.get('id', None)
        self._tags: list = kwargs.get('tags', [])
        self._items: list = []
        self._objects: list = []
        self._creatures: list = []

        self.shortdesc: str = kwargs.get('shortdesc', 'a blank room')
        self.longdesc: str = kwargs.get('longdesc', 'a blank, uneventful room')

    def __getitem__(self, item) -> [CanBeInWorld, None]:
        for i in self._items:
            i: Item
            if i.name == item: return i

        for o in self._objects:
            o: Object
            if o.name == item: return o

        for c in self._creatures:
            c: Creature
            if c.name == item: return c

        for i in self._items:
            i: Item
            if i.checkfortag(item): return i

        for o in self._objects:
            o: Object
            if o.checkfortag(item): return o

        for c in self._creatures:
            c: Creature
            if c.checkfortag(item): return c
