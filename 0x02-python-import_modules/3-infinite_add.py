#!/usr/bin/python3
from sys import argv


def main():

    var1 = 0
    if len(argv) == 1:
        print(0)
    else:
        for var2 in range(1, len(argv)):
            var1 = var1 + int(argv[var2])
        print(var1)

if __name__ == "__main__":
    main()
