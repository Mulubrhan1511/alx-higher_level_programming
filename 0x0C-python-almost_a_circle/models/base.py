#!/usr/bin/python3
"""
This class will be the base of all other classes
the goal of it is to manage id att in all future classes
and avoid duplicating the same code
"""

import csv
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """add id value if not none, otherwise add 1 to nb_obj"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        s = []
        mule = cls.__name__ +".json"
        if len(list_objs) != 0:
            for i in list_objs:
                s.append(cls.to_dictionary(i))
        with open(mule, "w") as f:
            f.write(cls.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """that writes the JSON string representation of list_objs to a file"""
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
