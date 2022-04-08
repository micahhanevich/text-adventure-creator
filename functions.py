from classes import *

def look(room: Room, args: str):
    args = args.split(' ')
    if len(args) == 0:
        out = f'You are in {room.longdesc}'
        for
