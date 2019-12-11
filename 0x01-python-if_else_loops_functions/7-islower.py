#!/usr/bin/python3
def islower(c):
    result = ''
    for char in c:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
