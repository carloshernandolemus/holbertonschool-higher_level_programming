#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        var1 = number * (-1)
    else:
        var1 = number
    var1 = var1 % 10
    print("{:d}".format(var1), end='')
    return(var1)
