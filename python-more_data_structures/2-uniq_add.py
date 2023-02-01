#!/usr/bin/python3


def uniq_add(my_list=[]):
    list = set(my_list)
    num = 0

    for idx in list:
        num += idx

    return (num)
