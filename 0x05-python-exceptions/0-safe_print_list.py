#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for var1 in range(x):
        try:
            print("{}".format(my_list[var1]), end="")
            var1 += 1
        except:
            exit
    print()
    return(var1)
