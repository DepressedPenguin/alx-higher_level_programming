#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for numbers in my_list:
            if count < x:
                print(numbers, end='')
                count += 1
        print()
    except Exception as z:
        pass
    return count
