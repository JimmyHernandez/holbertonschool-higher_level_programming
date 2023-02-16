#!/usr/bin/python3
"""
  Class to create and define a
    rectangle.
"""


class Rectangle:
    """
   A rectangle is a shape with four sides, four right angles,
                       and two dimensions: length and width."

 The class Rectangle is a blueprint for creating objects with
 the same properties (width, height, area, perimeter) and
 methods (__init__(), __str__(), __repr__(), __del__(), area(), perimeter())
 """

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
