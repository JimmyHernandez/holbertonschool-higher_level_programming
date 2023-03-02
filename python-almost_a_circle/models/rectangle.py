#!/usr/bin/python3
"""_Rectangle_"""
import json
from models.base import Base


class Rectangle(Base):
    """
       It creates a class Rectangle that inherits from BaseGeometry

       :param width: the width of the rectangle
       :param height: Height of the rectangle
       :param x: the x-axis position of the rectangle, defaults to 0 (optional)
       :param y: the y-axis position of the rectangle, defaults to 0 (optional)
       :param id: object id
       """

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # WIDTH

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # HEIGHT

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    # Y

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__y = value

    # X

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__x = value
