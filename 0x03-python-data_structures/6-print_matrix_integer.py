#!/usr/bin/python3
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i in range(len(x)):
            if i == len(x) - 1:
                print("{:d}".format(x[i]))
            else:
                print("{:d}".format(x[i]), end=' ')
    if not matrix:
        print()
