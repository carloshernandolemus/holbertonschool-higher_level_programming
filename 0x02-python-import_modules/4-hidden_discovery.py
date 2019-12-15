#!/usr/bin/python3
from sys import argv
import hidden_4


def main():

    for var1 in dir(hidden_4):
        if var1[0] != '_' and var1[1] != '_':
            print(var1)

if __name__ == "__main__":
    main()
