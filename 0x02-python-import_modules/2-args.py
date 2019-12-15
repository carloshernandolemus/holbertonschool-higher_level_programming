#!/usr/bin/python3
from sys import argv


def main():

    var1 = 1
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    for var2 in range(1, len(argv)):
        print("{:d}: ".format(var2), end='')
        var1 = var1 + 1
        print(argv[var2])

if __name__ == "__main__":
    main()
