#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    my_list.reverse()
    for idx in range(size):
        print("{:d}".format(my_list[idx]))
