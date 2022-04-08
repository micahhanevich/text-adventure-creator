import json
import cmd

class Game(cmd.Cmd):

    # Setting repeated prompt
    prompt = '\n>>'

    # Tell the player where they are at game start
    intro = ''

    # COMMANDS

    def do_go(self, arg):
        """Move in a cardinal direction\nUsage: go <direction>\nDirections: [N, S, E, W, Up, Down]"""
        pass

    def do_kill(self, arg):
        """Attempt to kill a creature in the room\nUsage: kill <description>\nDescription: Text description of enemy / creature"""
        pass

    def do_look(self, arg):
        """Look at the room in general or something specific\nUsage: look [<around>, <at> <description>]"""
        pass

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

    def do_exit(self, arg):
        """Close the game\nUsage: exit\nAltneratives: quit, close"""
        exit()

    def precmd(self, line: str) -> str:
        sline = line.split(' ')
        if sline[0] in ['quit', 'close']:
            self.do_exit(''.join(sline[1:]))

        return line

    def default(self, line: str) -> bool:
        print(f"What does '{line}' mean?")
        return False


game = Game()
game.cmdloop()
