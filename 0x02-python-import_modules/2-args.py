#!/usr/bin/python3
import sys
if __name__ == '__main__':
    z = sys.argv
    t = len(z) - 1
    if t == 0:
        print("{} arguments.".format(t))
    elif t == 1:
        print("{} argument:".format(t))
        print("{}: {}".format(t, z[1]))
    else:
        print("{} arguments:".format(t))
        for x in range(1, t + 1):
            print("{}: {}".format(x, z[x]))
