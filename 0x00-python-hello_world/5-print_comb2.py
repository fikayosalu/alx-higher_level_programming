#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("{i:02}, ".format(i), end="")
    else:
        print("{:d}".format(i))
