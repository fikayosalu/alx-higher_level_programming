#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    arr = sorted(a_dictionary)
    for i in arr:
        print("{}: {}".format(i, a_dictionary.get(i)))
