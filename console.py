#!/usr/bin/python3
"""
    import modules
"""
import cmd
import encodings
import sys
from sys import argv
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
import json
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


"""
    HBNB Command class file
"""


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        sys.exit()

    def emptyline(self):
        """Empty line command
        """
        pass

    def do_create(self, arg):
        """Create command creates a new instance of BaseModell
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            self = BaseModel()
            BaseModel.save(self)
            print(self.id)

    def do_show(self, arg):
        """Show command prints the string representation of an instance
based on the class name and id
        """
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(array) < 2:
            print("** instance id missing **")
        else:
            with open('file.json', 'r', encoding="utf-8") as fd:
                info = json.load(fd)
                for key in info:
                    ar = key.split(".")
                    if array[1] == ar[1]:
                        print(info.get("BaseModel.{}".format(ar[1])))
                if array[1] != ar[1]:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command deletes an instance based on the class name and id
        """
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(array) < 2:
            print("** instance id missing **")
        else:
            with open("file.json", "r", encoding="utf-8") as flj:
                list = json.load(flj)
                for key in list:
                    ar = key.split(".")
                    if array[1] == ar[1]:
                        new_list = "BaseModel.{}".format(ar[1])

                if array[1] != ar[1]:
                    print("** no instance found **")
                    return

            list.pop(new_list)
            with open("file.json", 'w', encoding="utf-8") as f:
                json.dump(list, f)

    def do_all(self, arg):
        """All command prints all string representation of all instances
        """
        array = arg.split()
        if len(array) < 1 or array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_list = []
            dict_obj = storage.all()
            for key, value in dict_obj.items():
                new_list.append(str(value))
            print(new_list)

    def do_update(self, arg):
        """Update command updates an instance based on the class name and id
        """
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
            return
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(array) < 2:
            print("** instance id missing **")
            return
        elif len(array) >= 2:
            with open("file.json", "r", encoding="utf-8") as flj:
                list = json.load(flj)
                new_key = ""
                for key in list:
                    ar = key.split(".")
                    if array[1] == ar[1]:
                        if len(array) < 3:
                            print("** attribute name missing **")
                            return
                        elif len(array) < 4:
                            print("** value missing **")
                            return
                        else:
                            new_key = f"BaseModel.{ar[1]}"
                if len(new_key) < 1:
                    print("** no instance found **")
                    return

        list[new_key].update({f"{array[2]}": f"{array[3]}"})
        with open("file.json", 'w', encoding="utf-8") as f:
            json.dump(list, f)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
