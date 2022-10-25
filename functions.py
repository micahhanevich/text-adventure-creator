from typing import overload
import json5 as json
import keyboard
from time import sleep
from classes import *
from structures import *

try:
    with open('settings', 'r') as f:
        settings: dict = load(f)
except FileNotFoundError:
    print('FATAL ERROR: 0002\nSettings could not be found')
    exit(1)


def customprint(string: str, txtspd: [str, TextSpeed] = settings['Text Speed']) -> None:
    if isinstance(txtspd, str):
        txtspd: TextSpeed = TextSpeed.getvalfromstr(txtspd)

    for c in string:
        print(c, end='', flush=True)
        sleep(txtspd.value)


def examine(room: Room, args: str, **kwargs) -> None:
    l_settings = kwargs.get('settings', settings)
    feature = room.find(args)
    if feature is None:
        customprint(f'I don\'t see a(n) "{args}" in here...', l_settings['Text Speed'])
    else:
        customprint(f'{feature.longgrammar} {feature.getdesc(Feature.Desc.LONG)}.', l_settings['Text Speed'])


def exit_game(**kwargs) -> None:
    l_settings = kwargs.get('settings', settings)
    customprint('\nExit Game?\n(Y/N)')
    if get_keyboard_input():
        customprint('\n\nClosing Game...')
        exit(0)
    else:
        customprint('\n\nGame exit cancelled.\n')


def get_keyboard_input(desiredkeypress: str = 'y', **kwargs) -> bool:
    l_settings = kwargs.get('settings', settings)
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key: str = event.name
            if key.lower() == desiredkeypress.lower():
                return True
            else:
                return False


def look(room: Room, args: str, **kwargs):
    l_settings = kwargs.get('settings', settings)
    args = args.strip()
    splargs = args.split(' ')
    if args == '':
        customprint(f'You are in {room.longgrammar} {room.getdesc(Feature.Desc.LONG)}.',
                    txtspd=l_settings['Text Speed'])
    elif splargs[0] == 'around':
        customprint(
            f'You are in {room.shortgrammar} {room.getdesc(Feature.Desc.SHORT)}.\n{roomprint(room)}' if len(
                room) > 0 else f'You are in {room.shortgrammar} {room.getdesc(Feature.Desc.SHORT)}.',
            txtspd=l_settings['Text Speed'])
    elif splargs[0] == 'at':
        examine(room, ' '.join(splargs[1:]))


def roomprint(room: Room, **kwargs) -> str:
    l_settings = kwargs.get('settings', settings)
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
    else:
        return 'There is nothing here...'

    return out


def settingscmd(args: str, **kwargs):
    l_settings = kwargs.get('settings', settings)
    splargs = args.split(' ')
    if args == '':

        barlen = 0
        keylen = 0
        lines = []
        for setting in l_settings:
            if len(setting) > keylen:
                keylen = len(setting)
        for setting in l_settings:
            lines.append(f'{setting}{" " * (keylen - len(setting) + 1)}= {l_settings[setting]}\n')
        for line in lines:
            if len(line) > barlen:
                barlen = len(line)

        customprint(f'SETTINGS\n{"-" * barlen}\n{"".join(lines)}{"-" * barlen}', TextSpeed.HYPER)

    elif splargs[0] == 'set':
        if l_settings.get(' '.join(splargs[1:-1])) is None:
            customprint(f'No Setting "{" ".join(splargs[1:-1])}"', TextSpeed.HYPER)
            return None

        l_settings[' '.join(splargs[1:(len(splargs) - 1)])] = splargs[-1]
        l_settings['Text Speed'] = TextSpeed.getvalfromstr(l_settings['Text Speed'])
        return l_settings


class CustomCmdHooks(CustomEnum):
    EXIT = exit_game
    PRINT = customprint


class Translator:
    def __init__(self):
        self._reader = json.JSONDecoder()

    def get_cmd(self, filepath: str):
        with open(filepath, 'r') as f:
            cmdjson = self._reader.decode('\n'.join(f.readlines()))
