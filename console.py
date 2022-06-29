#!/usr/bin/python3
"""
    import module
"""
import cmd
import sys
from sys import argv
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
import json


"""
    HBNB Command class file
"""


class HBNBCommand(cmd.Cmd):
    """ 
    class HBNBCommand
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program """
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program """
        sys.exit()

    def emptyline(self):
        """ empty line command """
        pass

    def do_create(self, arg):
        """create command creates a new instance of BaseModell"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            self = BaseModel()
            BaseModel.save(self)
            print(self.id)

    def do_show(self, arg):
        """
            show command prints the string representation of an instance
            based on the class name and id
        """
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
        elif array[0] != "BaseModel":
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
        """Deletes an instance based on the class name and id"""
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
        elif array[0] != "BaseModel":
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
                

    """def do_all(self, arg):
        Prints all string representation of all instances
        array = arg.split()
        if array[0] != "BaseModel":
            print("** class doesn't exist **")
        else:"""
            







if __name__ == '__main__':
    HBNBCommand().cmdloop()
