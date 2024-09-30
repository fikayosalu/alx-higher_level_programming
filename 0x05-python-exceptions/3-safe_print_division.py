#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except (TypeError, ValueError, ZeroDivisionError):
        return "None"
    finally:
        if b == 0:
            print("Inside result: {}".format("None"))
        else:
            print("Inside result: {:.1f}".format(a / b))
