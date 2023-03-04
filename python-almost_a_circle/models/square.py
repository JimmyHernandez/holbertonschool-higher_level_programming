#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
"""  The __init__ function is a constructor that initializes
                             the attributes of the class"""


class Square(Rectangle):
    """
        A function that updates the attributes of an instance.

        :param size: the size of the square
        :param x: x-axis position, defaults to 0 (optional)
        :param y: y-position, defaults to 0 (optional)
        :param id: the id of the square
    """

    def __init__(self, size, x=0, y=0, id=None):

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns string representation
        of the Square.
        """
        STR = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return (STR)

    @property
    def size(self):
        """
        Retrieves size attribute.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Sets size attribute to value.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of an instance.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation
        of a square.
        """
        MyDICT = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return (MyDICT)