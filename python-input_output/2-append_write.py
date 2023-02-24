#!/usr/bin/python3
"""_summary_ """


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'a+') as F:
        return (F.write(text))
