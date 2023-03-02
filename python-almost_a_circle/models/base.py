#!/usr/bin/python3
"""_summary_"""


class Base:
    """
        If the id is not an integer, raise a TypeError.
        If the id is not None, set the id to the id.
        If the id is None, increment the number of
        objects by 1 and set the id to the number of objects.
        """
    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
