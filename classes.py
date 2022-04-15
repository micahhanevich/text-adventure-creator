import enum


class Feature:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name', None)
        self._tags: list = kwargs.get('tags', [])
        self._shortdesc: str = kwargs.get('shortdesc', None)
        self._longdesc: str = kwargs.get('longdesc', None)

        self.grammar = kwargs.get('grammar', 'a')

    def checkfortag(self, tag: str) -> bool:
        if tag in self._tags: return True
        else: return False

    class Desc(enum.Enum):
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


class Object(Feature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


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

    def __getitem__(self, item) -> [Feature, None]:
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

    def __len__(self):
        return len(self._items) + len(self._objects) + len(self._creatures)


from structures import Rooms


class Player(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.location: dict = {'x': 0, 'y': 0, 'z': 0, 'room': Rooms.Nothing}
