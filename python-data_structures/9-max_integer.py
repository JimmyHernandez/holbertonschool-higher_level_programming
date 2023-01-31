#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == 0:
        return (None)

    size = len(my_list)
    int_max = my_list[0]
    for idx in range(1, size):
        if my_list[idx] > int_max:
            int_max = my_list[idx]

            return (int_max)
