#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    size = len(my_list)
    copy = my_list.copy()

    if idx < 0:
        return copy
    if idx > size - 1:
        return copy

    copy[idx] = element

    return (copy)
