#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
module = number % 10
modulen = number % -10
a = "Last digit of"
b = "and is less that 6 and not 0"
c = "and is greater than 5"
d = "and is 0"

if number > 1 and module < 6 and module != 0:
    print("{:s} {:d} is {:d} {:s}".format(a, number, module, b))
if number < -1 and modulen < 6 and modulen != 0:
    print("{:s} {:d} is {:d} {:s}".format(a, number, modulen, b))
if number > 1 and module > 5:
    print("{:s} {:d} is {:d} {:s}".format(a, number, module, c))
if number > 1 and module == 0:
    print("{:s} {:d} is {:d} {:s}".format(a, number, module, d))
if number < -1 and modulen == 0:
    print("{:s} {:d} is {:d} {:s}".format(a, number, module, d))
