#!/usr/bin/python3
"""
The above function is a class that defines a rectangle.
"""


class Rectangle:
    """
    :param width: the width of the rectangle
    :param height: Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):

        Rectangle = ""
        if self.height == 0 or self.width == 0:
            return ''
        str = ''
        for I in range(self.height):
            for J in range(self.width):
                str += '#'
            str += '\n'
        return str[:-1]

    def __repr__(self):

        return ("Rectangle({}, {})".format(self.width, self.height))

    # Width Property and Setter.
    @property
    def width(self):

        return (self.__width)

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Height Property and Setter
    @property
    def height(self):

        return (self.__height)

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return (self.width * self.height)

    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))
