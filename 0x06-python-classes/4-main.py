#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square2 = Square("error")
    print("Area: {} for size: {}".format(my_square.area(), my_square2.size))
except Exception as e:
    print(e)
