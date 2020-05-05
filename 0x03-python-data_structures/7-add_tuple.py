#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    var1 = tuple_a + (0, 0)
    var2 = tuple_b + (0, 0)
    var3 = ((var1[0] + var2[0]), (var1[1] + var2[1]))
    return(var3)
