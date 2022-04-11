import json

from classes import *
from json import *


def look(room: Room, args: str):
    args = args.strip(' ').split(' ')
    if args == ['']: args = []
    if len(args) == 0:
        out = f'You are in {room.longdesc}'
        test = json.load('resources/builtin/creatures/slime.creature')
        print('here')
        print(test)
