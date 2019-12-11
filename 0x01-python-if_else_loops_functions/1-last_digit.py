#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

var1 = number % 10
var2 = number * -1

str1 = "Last digit of"
str2 = "and is less than 6 and not 0"
str3 = "and is greater than 5"

if number < 0 and var1 != 0:
    print("{:s} {:d} is {:d} {:s}".format(str1, number, var2 % 10 * -1, str2))
if number > 0 and var1 != 0 and var1 < 6:
    print("{:s} {:d} is {:d} {:s}".format(str1, number, var1, str2))
if var1 == 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
if number > 0 and var1 > 5 and var1 != 0:
    print("{:s} {:d} is {:d} {:s}".format(str1, number, var1, str3))
