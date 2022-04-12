class Room:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.tags: list = kwargs.get('tags', [])
        self._items: list = []
        self._objects: list = []
        self._creatures: list = []

        self.shortdesc: str = kwargs.get('shortdesc', 'a blank room')
        self.longdesc: str = kwargs.get('longdesc', 'a blank, uneventful room')


class Creature:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name', None)
        self.tags: list = kwargs.get('tags', [])
        stats: dict = kwargs.get('stats', {})
        self.vit = stats.get('vit') if stats.get('vit') is not None else 1
        self.str = stats.get('str') if stats.get('str') is not None else 1
        self.dex = stats.get('dex') if stats.get('dex') is not None else 1
        self.end = stats.get('end') if stats.get('end') is not None else 1
        self.run = stats.get('run') if stats.get('run') is not None else 1
        self.shortdesc = kwargs.get('shortdesc', None)
        self.longdesc = kwargs.get('longdesc', None)

    def __str__(self):
        return '<class Creature>'

    # def __format__(self, format_spec):
    #     return f'<Creature {self.name} | vit: {self.vit} | str: {self.str} | dex: {self.dex} | end: {self.end} | run: {self.run}>'
