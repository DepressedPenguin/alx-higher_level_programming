#!/usr/bin/python3

def print_last_digit(number):
    last_de = abs(number) % 10
    return -last_de if number < 0 else last_de
