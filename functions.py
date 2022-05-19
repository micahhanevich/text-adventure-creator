import json
from time import sleep
from classes import *
from classes import Feature
from structures import *


def customprint(string: str, txtspd: TextSpeed = TextSpeed.NORMAL):
    for c in string:
        print(c, end='', flush=True)
        sleep(txtspd.value)


def examine(room: Room, settings: dict, args: str):
    feature = room.find(args)
    if feature is None:
        customprint(f'I don\'t see a "{args}" in here...', settings['Text Speed'])
    else:
        customprint(f'{feature.longgrammar} {feature.getdesc(Feature.Desc.LONG)}.', settings['Text Speed'])


def look(room: Room, settings: dict, args: str):
    args = args.strip()
    splargs = args.split(' ')
    if args == '':
        customprint(f'You are in {room.longgrammar} {room.getdesc(Feature.Desc.LONG)}.', txtspd=settings['Text Speed'])
    elif splargs[0] == 'around':
        customprint(f'You are in {room.shortgrammar} {room.getdesc(Feature.Desc.SHORT)}.\n{roomprint(room, settings)}' if len(room) > 0 else f'You are in {room.shortgrammar} {room.getdesc(Feature.Desc.SHORT)}.', txtspd=settings['Text Speed'])
    elif splargs[0] == 'at':
        examine(room, settings, ' '.join(splargs[1:]))


def roomprint(room: Room, settings: dict) -> str:
    out = ''
    lroom = len(room)
    features = room.getfeatures()
    if lroom == 1:
        feature: Feature = features[0]
        out += f'There is {feature.shortgrammar} {feature.getdesc(Feature.Desc.SHORT)}.'
    elif lroom == 2:
        out += f'There is {features[0].shortgrammar} {features[0].getdesc(Feature.Desc.SHORT)}\nand {features[1].shortgrammar} {features[1].getdesc(Feature.Desc.SHORT)}'
    elif lroom == 3:
        out += f'There is {features[0].shortgrammar} {features[0].getdesc(Feature.Desc.SHORT)},\n{features[1].shortgrammar} {features[1].getdesc(Feature.Desc.SHORT)},\nand {features[1].shortgrammar} {features[1].getdesc(Feature.Desc.SHORT)}'
    elif lroom > 3:
        out += f'There is '
        for feature in features[0:-1]:
            out += f'{feature.shortgrammar} {feature.getdesc(Feature.Desc.SHORT)},\n'
        out += f'and {features[-1].shortgrammar} {features[-1].getdesc(Feature.Desc.SHORT)}'
    else: return 'There is nothing here...'

    return out


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

    
class CustomCmdHooks(CustomEnum):
    EXIT = exit
    PRINT = customprint


class Translator:
    def __init__(self):
        self._reader = json.JSONDecoder()

    def get_cmd(self, filepath: str):
        with open(filepath, 'r') as f:
            cmdjson = self._reader.decode('\n'.join(f.readlines()))

