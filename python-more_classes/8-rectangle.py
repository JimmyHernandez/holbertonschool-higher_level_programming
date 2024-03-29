#!/usr/bin/python3
"""
A static method that returns the biggest rectangle based on the area.
"""


class Rectangle:
    """
    :param width: The width of the rectangle
    :param height: Height of the rectangle
    """
    number_of_instances = 0

    print_symbol = '#'

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
                str += str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
