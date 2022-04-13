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
    splargs = args.split(' ')
    if args == '':

        barlen = 0
        keylen = 0
        lines = []
        for setting in settings:
            if len(setting) > keylen: keylen = len(setting)
        for setting in settings:
            lines.append(f'{setting}{" " * (keylen - len(setting) + 1)}= {settings[setting]}\n')
        for line in lines:
            if len(line) > barlen: barlen = len(line)

        customprint(f'SETTINGS\n{"-" * barlen}\n{"".join(lines)}{"-" * barlen}', TextSpeed.HYPER)

    elif splargs[0] == 'set':
        if settings.get(' '.join(splargs[1:-1])) is None:
            customprint(f'No Setting "{" ".join(splargs[1:-1])}"', TextSpeed.HYPER)
            return None

        settings[' '.join(splargs[1:(len(splargs) - 1)])] = splargs[-1]
        settings['Text Speed'] = TextSpeed.getvalfromstr(settings['Text Speed'])
        return settings
