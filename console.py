#!/usr/bin/python3
"""module of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_list = {"BaseModel": BaseModel,
              "User": User,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review
              }
white_list = []
for key in class_list:
    white_list.append(key)
commands = ["do_show",
            "do_destroy",
            "do_all",
            "do_update",
            "do_count"
            ]


class HBNBCommand(cmd.Cmd):
    """Representation of a HBNBCommand"""

    prompt = "(hbnb) "

    def emptyline(self):
        return False

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_create(self, line):
        """creates a new instance of BaseModel, saves it and prints the id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        else:
            for key, value in class_list.items():
                if args[0] == key:
                    new_instance = value()
                    print(new_instance.id)
                    new_instance.save()

def do_show(self, line):
        """prints the string representation of an instance
           based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] in objects_dic:
            print(objects_dic[args[0]+"."+args[1]])
        else:
            print("** no instance found **")

def do_destroy(self, line):
        """deletes an instance based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] in objects_dic:
            storage.all().pop(args[0]+"."+args[1])
            storage.save()
        else:
            print("** no instance found **")

def do_all(self, line):
        """prints all string representation of all instances
           based (or not) on the class name"""
        args = line.split()
        objects_dic = storage.all()
        objects_list = []
        if len(args) == 0:
            for key in objects_dic:
                objects_list.append(objects_dic[key].__str__())
            print(objects_list)
        elif args[0] in white_list:
            for key in objects_dic:
                if objects_dic[key].__class__.__name__ == args[0]:
                    objects_list.append(objects_dic[key].__str__())
            print(objects_list)
        else:
            print("** class doesn't exist **")