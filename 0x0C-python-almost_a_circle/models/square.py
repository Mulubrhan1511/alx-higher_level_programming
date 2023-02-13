#!/usr/bin/python3
"""
class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square and inherits som attrs from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """test"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ string representation of a rectangle"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """square size"""
        return self.width

    @size.setter
    def size(self, value):
        """quare size getter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """return Square dictionary represntation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
