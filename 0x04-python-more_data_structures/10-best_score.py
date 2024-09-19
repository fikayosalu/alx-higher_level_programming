#!/usr/bin/python3
def best_score(a_dictionary):
    high = float("-inf")

    if a_dictionary:
        for i, j in a_dictionary.items():
            if high < j:
                high = j
        for a, b in a_dictionary.items():
            if high == b:
                return (a)
    else:
        return "None"
