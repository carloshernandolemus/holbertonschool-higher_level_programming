#!/usr/bin/python3
def raise_exception():
    try:
        var1 = "Raise"
        print(var1 / 2)
    except TypeError:
        raise TypeError
