#!/usr/bin/python3
"""Function that open a file"""


def read_file(filename=""):
    """Function open"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
