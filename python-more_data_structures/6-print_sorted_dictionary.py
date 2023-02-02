#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    nlist = list(a_dictionary.keys())
    nlist.sort()

    for KEYS in nlist:
        print("{}: {}".format(KEYS, a_dictionary.get(KEYS)))
