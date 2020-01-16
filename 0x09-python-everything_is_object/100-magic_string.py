#!/usr/bin/python3
def magic_string():
    var1 = 0
    magic_string.var1 = getattr(magic_string, "var1", 0) + 1
    return ("Holberton, " * (magic_string.var1 - 1) + "Holberton")
