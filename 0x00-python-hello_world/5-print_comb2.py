#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("{:d}, ".format(i), end="")
    else:
        print("{:d}".format(i))
