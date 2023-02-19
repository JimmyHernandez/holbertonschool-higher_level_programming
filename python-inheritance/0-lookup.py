#!/usr/bin/python3
""" It takes an object as an argument and returns a list
             of the attributes and methods of that object
"""


def lookup(obj):
    """
    obj: The object to be inspected
    eturn: A list of all the attributes and methods of the object.
    """
    list = dir(obj)
    return (list)
