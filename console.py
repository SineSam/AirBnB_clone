#!/usr/bin/python3

"""Define the HBNBC class"""
import cmd
import readline
import shlex
import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
        "Amenity": Amenity,
        "baseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
        }


class HBNBCommand(cmd.Cmd):
    """
    A class representing the console commands
    """
    prompt = "(hbnb) "

    def do_help(self, args):
        """Provides help for commands"""
        if args:
            super().do_help(args)
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            commands = [cmd for cmd in dir(self) if cmd.startswith('do_')]
            for command in commands:
                docstring = getattr(self, command).__doc__
            print(f"{commands[3:]}")

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles end of file"""
        print()
        return True

    def do_creat(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name is missing **")
            return False
        if arg[0] in classes:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("**no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        arg = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif arg[0] in classes:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """
        arg = shlex.split(args)
        obj_list = []
        if len(arg) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[arg[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        arg = shlex.split(args)
        integers = [
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night"
            ]
        floats = ["latitude", "longitude"]
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] in classses:
            if len(arg) > 1:
                k = arg[0] + "." + arg[1]
                if k in models.storage.all():
                    if len(arg) > 2:
                        if len(arg) > 3:
                            if arg[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        arg[3] = int(args[3])
                                    except KeyError as e:
                                        args[3] = 0
                                elif arg[2] in floats:
                                    try:
                                        arg[3] = float(arg[3])
                                    except AttributeError as e:
                                        arg[3] = 0.0
                            setattr(models.storage.all()[k], arg[2], arg[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
