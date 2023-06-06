#!/usr/bin/python3

import random

number = random.randint(-10, 10)

if int(number) > 0:
    print(number, "is positive")
elif int(number) == 0:
    print(number, "is zero")
elif int(number) < 0:
    print(number, "is negative")
