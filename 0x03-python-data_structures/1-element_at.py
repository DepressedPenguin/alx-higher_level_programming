#!/usr/bin/python3

def element_at(my_list, idx):
    if int(idx) < 0:
        print("None")
    elif int(idx) > len(my_list):
        print("None") 
    for x in my_list[:]:
        if len(my_list) >= int(idx) >= 0 and x == my_list[idx]:
            print("Element at index {:d} is {}".format(idx,x))
