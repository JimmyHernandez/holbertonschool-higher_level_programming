#!/usr/bin/python3
"""_Rectangle_"""
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

    # WIDTH-------------------------------------------

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

    # HEIGHT------------------------------------------

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Y-----------------------------------------------

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # X-----------------------------------------------

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

# Public methods

    def area(self):
        """
        The function area() returns the area of the rectangle
        :return: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """Printing the rectangle."""

        for y in range(0, self.__y):
            print()

        for height in range(0, self.__height):

            for x in range(0, self.__x):
                print(" ", end="")

            for width in range(0, self.__width):
                print("#", end="")
            print()

        def __str__(self):
            """ A string that is being formatted. """
        str = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                      self.__x, self.__y, self.__width, self.__height)
        return (str)
