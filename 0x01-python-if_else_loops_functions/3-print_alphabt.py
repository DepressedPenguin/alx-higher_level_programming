#!/usr/bin/python3
for b in range(97, 123):
    if b == 113 or b == 101:
        continue
    print("{}".format(chr(b)), end='')
