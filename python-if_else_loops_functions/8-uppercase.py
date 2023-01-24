#!/usr/bin/python3
def uppercase(str):
    for Char in range(len(str)):
        if ord(str[Char]) >= 97 and ord(str[Char]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[Char]) - num), end='')
    print()
