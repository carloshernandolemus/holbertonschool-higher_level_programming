#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list1 = list(a_dictionary.keys())

    for value1 in list1:
        if value == a_dictionary.get(value1):
            del a_dictionary[value1]

    return (a_dictionary)
