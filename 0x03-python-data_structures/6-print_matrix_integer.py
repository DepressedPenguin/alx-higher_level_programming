#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for value in x:
            print("{:d}".format(value), end=' ')
    print()
