#!/usr/bin/python3


def multiple_returns(sentence):
    size = len(sentence)

    if (size == 0):
        newt = (size, None)
    else:
        newt = (size, sentence[0])
    return (newt)
