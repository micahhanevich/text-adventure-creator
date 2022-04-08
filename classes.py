class Room:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.tags: list = kwargs.get('tags', [])
        self._items: list = []
        self._objects: list = []
        self._creatures: list = []

        self.shortdesc: str = kwargs.get('shortdesc', 'a blank room')
        self.longdesc: str = kwargs.get('longdesc', 'a blank, uneventful room')

class Object:
    def __init__(self, **kwargs):
        pass
