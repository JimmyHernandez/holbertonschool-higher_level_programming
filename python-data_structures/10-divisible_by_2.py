#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    div = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            div.append(True)
        else:
            div.append(False)

    return (div)
