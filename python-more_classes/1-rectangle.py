#!/usr/bin/python3
""" The class Rectangle is a blueprint for creating
                 objects that represent rectangles.
    """


class Rectangle:
    """
    The function __init__ is a constructor that
    initializes the attributes of the class

    :param width: The width of the rectangle,
                     defaults to 0 (optional)

    :param height: The height of the rectangle,
                     defaults to 0 (optional)
    """

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

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
