#!/usr/bin/python3
def raise_exception():
    try:
        var1 = "Hello World"
        print(var1 / 2)
    except TypeError:
        raise TypeError
