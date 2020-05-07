#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    var1 = sorted(a_dictionary.keys())
    for i in var1:
        print("{}: {}".format(i, a_dictionary[i]))
