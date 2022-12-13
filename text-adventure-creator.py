from typing import TextIO

import json5 as json
import cmd as CMD
from functions import *
from structures import *
from os import listdir


char = Player()


class Game(CMD.Cmd):

    def __init__(self):
        super().__init__()

        try:
            debug: bool = settings['Debug']
            if type(debug) != bool:
                raise KeyError
        except (KeyError, AttributeError):
            settings.update({'Debug': False})

        try:
            txtspd: TextSpeed = TextSpeed.getvalfromstr(settings['Text Speed'].upper())
            if txtspd is None:
                raise KeyError
            else:
                settings.update({'Text Speed': txtspd.name})
        except (KeyError, AttributeError):
            settings.update({'Text Speed': TextSpeed.NORMAL.name})

        Game.update_settings()

    # Setting repeated prompt
    prompt = '\n<~~°~~>\n>>'

    # Tell the player where they are at game start
    intro = ''

    # Store command aliases
    aliases = {}
    qrefalias = {}

    # COMMANDS

    def do_go(self, arg):
        """Move in a cardinal direction\nUsage: go <direction>\nDirections: [N, S, E, W, Up, Down]"""
        pass

    def do_kill(self, arg):
        """Attempt to kill a creature in the room\nUsage: kill <description>\nDescription: Text description of enemy / creature"""
        pass

    def do_look(self, arg):
        """Look at the room in general or something specific\nUsage: look [<around>, <at> <description>]"""
        look(char.location['room'], arg)

    def do_drop(self, arg):
        """Attempt to drop an item\nUsage: drop <description>\nDescription: Text description of item"""
        pass

    def do_take(self, arg):
        """Attempt to take an item\nUsage: take <description>\nDescription: Text description of item"""
        pass

    def do_examine(self, arg):
        """Get a closer look at an object\nUsage: examine <description>\nDescription: Text description of object"""
        pass

    def do_equip(self, arg):
        """Equip a piece of equipment from your inventory\nUsage: equip <description>\nDescription: Text description of equipment in inventory"""
        pass

    def do_equipped(self, arg):
        """Check what gear you have equipped\nUsage: equipped"""
        pass

    def do_carrying(self, arg):
        """Check your inventory\nUsage: carrying"""
        pass

    def do_settings(self, arg):
        """Check / change settings"""
        setval = settingscmd(arg)
        if setval is not None:
            Game.update_settings()

    def do_exit(self, arg):
        """Close the game\nUsage: exit\nAltneratives: quit"""
        exit_game()
        pass

    @staticmethod
    def update_settings() -> None:
        with open('settings', 'w') as f:
            dump(settings, f)

    def precmd(self, line: str) -> str:
        sline = line.split(' ')
        for alias in self.qrefalias.keys():
            if alias == line:
                getattr(self, str(self.qrefalias[alias][0]))(self.qrefalias[alias][1])
        return line

    def preloop(self) -> None:
        try:
            ldir = []
            for file in listdir('resources/builtin/commands'):
                if file.endswith('.command'):
                    ldir.append(file)
            for builtincmd in ldir:
                with open('resources/builtin/commands/' + builtincmd, 'r') as cmd:
                    try:
                        cmd = load(cmd)
                        self.aliases.update({builtincmd: cmd})
                        for alias in cmd['command_settings']['aliases']:
                            self.qrefalias.update({alias: [cmd['command_settings']['function'], cmd['command_settings']['default_params']]})
                    except json.decoder.JSONDecodeError as e:
                        customprint('\n!WARNING! - Command resources/builtin/commands/' + builtincmd + ' was not formatted properly and failed to load\n', TextSpeed.INSTANT)
        except FileNotFoundError as e:
            if settings['Debug']:
                customprint('FATAL ERROR: 0001\nBuiltins could not be found', TextSpeed.INSTANT)
            if settings['Dev']:
                customprint(e, TextSpeed.INSTANT)
            exit(1)

    def default(self, line: str) -> bool:
        print(f"What does '{line}' mean?")
        return False


class DebugGame(Game):

    def do_test(self, arg):
        pass


class DevGame(DebugGame):

    def do_pycmd(self, arg):
        """Dev command only\nAttempt to run `arg` as raw python\nWARNING: potentially insecure"""
        exec(arg)


# c = Cell(Rooms.StartCell.value)

try:
    with open('settings', 'r') as f:
        settings: dict = load(f)
except FileNotFoundError:
    customprint('FATAL ERROR: 0002\nSettings could not be found', TextSpeed.INSTANT)
    exit(1)

if settings['Dev']:
    game: DevGame = DevGame()
elif settings['Debug']:
    game: DebugGame = DebugGame()
else:
    game: Game = Game()

game.cmdloop()
