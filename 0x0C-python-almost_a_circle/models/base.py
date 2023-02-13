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
        """create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        file = []
        try:
            with open(filename, 'r') as fi:
                file = cls.from_json_string(fi.read())
            for i, e in enumerate(file):
                file[i] = cls.create(**file[i])
        except:
            pass
        return file

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """using csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """using cvf"""
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """that opens a window and draws all the"""
        rectangles = turtle.Turtle()
        for i in list_rectangles:

            rectangles.forward(i.width)
            rectangles.left(90)
            rectangles.forward(i.height)
            rectangles.left(90)
            rectangles.forward(i.width)
            rectangles.left(90)
            rectangles.forward(i.height)
            rectangles.penup()
            rectangles.forward(150)

            rectangles.pendown()
        rectangles.penup()
        rectangles.forward(150)

        rectangles.pendown()
        for i in list_squares:

            rectangles.forward(i.size)
            rectangles.left(90)
            rectangles.forward(i.size)
            rectangles.left(90)
            rectangles.forward(i.size)
            rectangles.left(90)
            rectangles.forward(i.size)
            rectangles.penup()
            rectangles.forward(100)
            rectangles.left(180)
            rectangles.pendown()
        turtle.done()    
