#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    var1 = 0
    for var2 in range(x):
        try:
            print("{}".format(my_list[var2]), end="")
            var1 += 1
        except:
            break
    print()
    return var1
