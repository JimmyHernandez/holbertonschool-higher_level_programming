#!/usr/bin/python3
"""
base_geometry Class that defines the
attributes of Shapes.
"""


class BaseGeometry:
    """
    Public Instance Method: def area(self).
    Public Instance Method: def integer_validator(self, name, value).
    """

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
