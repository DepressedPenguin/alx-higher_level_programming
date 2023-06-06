#!/usr/bin/python3
for j in range(0, 100):
    print("{:02d}".format(j), end=', 'if j < 99 else '\n')
