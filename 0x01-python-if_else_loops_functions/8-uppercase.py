#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for var1 in range(len(str)):
        if ord(str[var1]) >= 97 and ord(str[var1]) <= 122:
            x = ord(str[var1]) - 32
        else:
            x = ord(str[var1])
        print("{:c}".format(x), end='')
