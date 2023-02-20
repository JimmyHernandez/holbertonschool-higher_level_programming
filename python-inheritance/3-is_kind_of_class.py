#!/usr/bin/python3
""" Return True if the object is an instance of
    the specified class ; otherwise return False .
"""


def is_kind_of_class(obj, a_class):
    """
    The isinstance() function takes two arguments:

    The object to check.
    The class to check against.
    If the object is an instance of the specified class,
    isinstance() returns True . Otherwise, it
    returns False

    :param obj: an object
    :param a_class: a class object
    :return: True or False
    """

    return isinstance(obj, a_class)
