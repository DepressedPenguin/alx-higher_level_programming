#!/usr/bin/python3
import random

# By DepressedPenguin (Zakaria Elaroussi)

number = random.randint(-10000, 10000)
lastofdigit = abs(number) % 10

if number > 0 or number == 0:
    if lastofdigit > 5:
        print(f"Last digit of {number} is {lastofdigit} and is greater than 5")
    elif lastofdigit == 0:
        print(f"Last digit of {number} is {lastofdigit} and is 0")
    elif lastofdigit < 6 and lastofdigit != 0:
        print("Last digit of {} is {} and is less than 6 "
              "and not 0".format(number, abs(lastofdigit)))
else:
    print("Last digit of {} is -{} and is less than 6 "
          "and not 0".format(number, abs(lastofdigit)))
