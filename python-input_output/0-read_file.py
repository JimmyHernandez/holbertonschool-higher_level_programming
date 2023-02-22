#!/usr/bin/python3
"""
This function reads a file and prints it to stdout
"""


def read_file(filename=""):
    """
    :param filename: the name of the file to read
    """
    with open('filename', encoding="utf-8") as f:
        readTxt = f.read()
        print(readTxt, end="")
