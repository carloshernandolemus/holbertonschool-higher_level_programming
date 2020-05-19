#!/usr/bin/python3
def magic_calculation(a, b):
    e = 0
    for var1 in range(1, 3):
        try:
            if (var1 > a):
                raise Exception('Too far')
            else:
                e += a ** b / var1
        except:
            e = b + a
            break
    return(equal)
