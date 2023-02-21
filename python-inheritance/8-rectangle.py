#!/usr/bin/python3
"""
__init__ is a constructor that initializes the attributes of the class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        :param width: The width of the rectangle
        :param height: The height of the rectangle
        """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__heigth = height
