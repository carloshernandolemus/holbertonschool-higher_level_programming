#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    var1 = []
    for x in matrix:
        var2 = list(map(lambda mult: mult**2, x))
        var1.append(var2)
    return(var1)
