#!/usr/bin/python3
"""
 Print_sorted prints the elements of the list
"""


class MyList(list):
    """
     Print_sorted prints the elements of the list.
    """

    def print_sorted(self):
        print(sorted(self))
