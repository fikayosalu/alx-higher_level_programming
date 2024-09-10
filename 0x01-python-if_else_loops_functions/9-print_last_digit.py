#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastdigit = (number * -1) % 10
        lastdigit = lastdigit * -1
        return lastdigit
    elif number >= 0:
        lastdigit = number % 10
        return lastdigit
