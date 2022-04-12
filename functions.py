import json
from time import sleep
from classes import *
from structures import *


def customprint(string: str, txtspd: TextSpeed):
    for c in string:
        print(c, end='', flush=True)
        sleep(txtspd.value)


def look(room: Room, settings: dict, args: str):
    args = args.strip(' ').split(' ')
    if args == ['']: args = []
    if len(args) == 0:
        customprint(f'You are in {room.longdesc}', txtspd=settings['Text Speed'])


def settings(settings: dict, args: str):
    if args == '':
        fline0 = f'Text Speed = {settings["Text Speed"].name}'
        lfline0 = len(fline0)
        print(f'\nSETTINGS\n{"-" * lfline0}\nText Speed = {settings["Text Speed"].name}\n{"-" * lfline0}')
