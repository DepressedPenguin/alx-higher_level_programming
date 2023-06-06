#!/usr/bin/python3
for j in range(0, 10, 1):
    for x in range(0, 10):
        if j == x or j < x:
            print("{}{}".format(j, x), end='\n' if j == 8 and x == 9 else ', ')
