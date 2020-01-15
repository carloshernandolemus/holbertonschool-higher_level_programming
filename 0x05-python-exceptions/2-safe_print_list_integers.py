#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        var1 = 0
        for var2 in range(x):
            if isinstance(my_list[var2], int):
                print("{:d}".format(my_list[var2]), end="")
                var1 += 1
        print()
        return(var1)
    except TypeError:
        pass
