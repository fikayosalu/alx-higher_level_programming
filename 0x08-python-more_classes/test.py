#!/usr/bin/python3
string = ["C", "is", "fun"]
def loop(width, height):
    display = []
    for i in range(height):
        j = 0
        while j < width:
            display.append(string)
            j += 1
        if i < height - 1:
            display.append('\n')
    array = "".join(map(str,display))
    print(array)


loop(3,5)
