#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for numbers in matrix:
        copy.append([numbers[i] * numbers[i]for i in range(len(numbers))])
    return copy
