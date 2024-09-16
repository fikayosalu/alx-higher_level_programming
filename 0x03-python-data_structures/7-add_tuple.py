#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #for tuple a length = 0
    if len(tuple_a) == 0:
        first = 0 + tuple_b[0]
       second = 0 + tuple_b[1]

    #for tuple_a length = 1
    if len(tuple_a) == 1:
        first = tuple_a[0] + tuple_b[0]
        second = 0 + tuple_b[1]
    #for tuple_b length = 0
    if len(tuple_b) == 0:
        first = tuple_a[0] + 0
        second = tuple_a[1] + 0
    #for tuple_b length = 1
    if len(tuple_b) == 1:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1] + 0

    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]
    return (first, second)
