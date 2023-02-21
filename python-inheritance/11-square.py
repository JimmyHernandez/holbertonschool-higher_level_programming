#!/usr/bin/python3
"""
Square inherits from Rectangle,
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """__init__ method takes a size parameter, which is validated
 by the integer_validator method from the parent class.
    """

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):

        return super().area()

    def __str__(self):

        return "[Square] {}/{}".format(self.__size, self.__size)
