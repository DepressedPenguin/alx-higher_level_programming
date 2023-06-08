#!/usr/bin/python3
import sys
loop = 0
i = 1
z = sys.argv
t = len(z) - 1
while i != len(z):
    loop = loop + int(z[i])
    i += 1
print(loop)
