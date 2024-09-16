#!/usr/bin/python3
def no_c(my_string):
    noC = ""
    for i in my_string:
        if i != "c" and i != "C":
            noC += i
    return noC
