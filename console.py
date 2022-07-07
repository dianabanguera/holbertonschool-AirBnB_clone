#!/usr/bin/python3
"""The console - AirBnB clone"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
import shlex
from datetime import datetime
import re


class HBNBCommand(cmd.Cmd):
    """Initialize the class"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "City",
               "Place", "State", "Amenity", "Review"]

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

    def do_create(self, line):
        """Method create"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(line)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Method Show"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            new_line = line.split(" ")
            if new_line[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(new_line) < 2:
                print("** instance id missing **")
            else:
                key = f"{new_line[0]}.{new_line[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Method destry"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            new_line = line.split(" ")
            if new_line[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(new_line) < 2:
                print("** instance id missing **")
            else:
                key = f"{new_line[0]}.{new_line[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Method All"""
        if line == "":
            data = [str(obj) for k, obj in storage.all().items()]
            print(data)
        else:
            if line not in self.classes:
                print("** class doesn't exist **")
            else:
                data = [str(obj) for k, obj in storage.all().items()
                        if type(obj).__name__ == line]
                print(data)

    def do_update(self, line):
        """Method update"""
        new_line = shlex.split(line)

        if len(new_line) == 0:
            print("** class name missing **")
        elif new_line[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(new_line) == 1:
            print("** instance id missing **")
        else:
            key = f"{new_line[0]}.{new_line[1]}"
            data = storage.all().get(key)
            if data is None:
                print("** no instance found **")
            elif len(new_line) == 2:
                print("** attribute name missing **")
            elif len(new_line) == 3:
                print("** value missing **")
            else:
                new_line[3] = self.typer(new_line[3])
                setattr(data, new_line[2], new_line[3])
                setattr(data, "updated_at", datetime.now())
                storage.save()

    def typer(self, value):
        """Typer method"""
        if value.isdigit():
            return int(value)
        if value.replace(".", "", 1).isdigit():
            return float(value)
        return value

    def default(self, line):
        """
        If the command is not recognized, check
        if the syntax is: <class name>.<method name> or not,
        if the class name and the method name exists will be executed
        """
        if "." in line:
            command = re.split(r"\.|\(|\)", line)

            if command[0] in self.classes:
                if command[1] == "show":
                    self.do_show(f"{command[0]} {command[2][1:-1]}")
                elif command[1] == "destroy":
                    self.do_destroy(f"{command[0]} {command[2][1:-1]}")
                elif command[1] == "count":
                    print(len(self.get_instances(command[0])))
                elif command[1] == "all":
                    print(self.get_instances(command[0]))

    def get_instances(self, object=""):
        """Gets the objects of the specified class"""
        instances = storage.all()

        if object:
            key = instances.keys()
            return [str(val) for key, val in instances.items()
                    if key.startswith(object)]
        return [str(val) for key, val in instances.items()]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
