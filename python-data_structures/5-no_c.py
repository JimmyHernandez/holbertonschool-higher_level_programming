#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string)
    newStr = my_string[:]
    string = 0

    for idx in range(size):
        if (my_string[idx] == 'c' or my_string[idx] == 'C'):
            newStr = newStr[:(idx - string)] + my_string[(idx + 1):]
            string += 1
    return (newStr)
