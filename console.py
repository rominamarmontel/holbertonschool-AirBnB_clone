#!/usr/bin/python3
"""
    import module
"""
import cmd
import sys
from models.base_model import BaseModel
import models


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

    def do_create(self, arg):
        """create command creates a new instance of BaseModell"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            BaseModel()
            models.save()
            print(f"{self.id}")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
