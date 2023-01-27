#!/usr/bin/python3
import sys
if __name__ == "__main__":

n = len(sys.argv)

print("{} arguments:".format(n - 1))

for idx in range(1, n):
    print("{}: {} ".format(idx, sys.argv[idx]))
