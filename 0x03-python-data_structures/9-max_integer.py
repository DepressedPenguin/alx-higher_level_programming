#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        print("None")
        return
    maxvalue = my_list[0]
    for number in my_list:
        if number > maxvalue:
            maxvalue = number
    return maxvalue
