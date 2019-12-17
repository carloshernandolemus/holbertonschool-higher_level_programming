#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    var1 = my_list
    for x in var1[::-1]:
        print("{:d}".format(x))
