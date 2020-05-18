#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        var1 = a / b
    except:
        var1 = None
    print("Inside result: {}".format(var1))
    return(var1)
