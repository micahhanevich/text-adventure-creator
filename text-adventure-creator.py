import json
from json import *
import cmd
from functions import *
from structures import *
from os import listdir


char = Player()


class Game(cmd.Cmd):

    def __init__(self):
        super().__init__()
        with open('settings', 'r') as f:
            settings: dict = load(f)
        self.settings: dict = settings

        debug = False
        try:
            debug: bool = self.settings['Debug']
            txtspd: TextSpeed = TextSpeed.getvalfromstr(self.settings['Text Speed'].upper())
        except KeyError:
            with open('settings', 'w') as f:
                dump({'Debug': False, 'Text Speed': TextSpeed.NORMAL.name}, f)
            txtspd = TextSpeed.NORMAL

        if txtspd is not None:
            self.settings['Text Speed'] = txtspd
        else:
            with open('settings', 'w') as f:
                for key in settings:
                    if key == 'Text Speed': settings[key] = TextSpeed.NORMAL.name
                dump(settings, f)

        self.settings['Debug'] = debug

    # Setting repeated prompt
    prompt = '\n\n>>'

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
        look(char.location['room'], self.settings, arg)

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
        setval = settings(self.settings, arg)
        if setval is not None:
            with open('settings', 'w') as f:
                dump(setval, f)

    def do_exit(self, arg):
        """Close the game\nUsage: exit\nAltneratives: quit, close"""
        exit()

    def precmd(self, line: str) -> str:
        sline = line.split(' ')
        for alias in self.qrefalias:
            if alias == line:
                getattr(self, self.qrefalias[alias][0])(self.qrefalias[alias][1])
        return line

    def preloop(self) -> None:
        for builtincmd in listdir('resources/builtin/commands'):
            with open('resources/builtin/commands/' + builtincmd, 'r') as cmd:
                cmd = load(cmd)
                self.aliases.update({builtincmd: cmd})
                for alias in cmd['aliases']:
                    self.qrefalias.update({alias: [cmd['function'], cmd['default_params']]})

    def default(self, line: str) -> bool:
        print(f"What does '{line}' mean?")
        return False


c = Cell(Rooms.StartCell.value)
game = Game()
game.cmdloop()
