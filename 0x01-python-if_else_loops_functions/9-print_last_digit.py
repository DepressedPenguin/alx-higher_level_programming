#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = abs(number)
    last_de = number % 10
    print("{}".format(last_de), end="")
    return last_de
