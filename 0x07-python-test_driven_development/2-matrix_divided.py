#!/usr/bin/python3
def matrix_divided(matrix, div):

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    size = 0

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg1)

    for j in matrix:
        if not j or not isinstance(j, list):
            raise TypeError(msg1)

        for k in j:
            if not type(k) in (int, float):
                raise TypeError(msg1)

        if size != 0 and len(j) != size:
            raise TypeError(msg2)
        size = len(j)

    rs = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return(rs)
