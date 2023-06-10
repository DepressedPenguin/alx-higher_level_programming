#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for i, x in enumerate(my_list):
        if int(idx) == x:
            my_list.pop(i)
            my_list.insert(i, element)
            print("{}".format(my_list))
            break
