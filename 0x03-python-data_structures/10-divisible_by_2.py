#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    var1 = []
    for x in my_list:
        if x % 2 == 0:
            var1.append(True)
        else:
            var1.append(False)
    return(var1)
