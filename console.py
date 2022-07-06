#!/usr/bin/python3
"""The console - AirBnB clone"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Initialize the class"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """End of file with a white space"""
        print()
        return True

    def emptyline(self):
        """Print an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
