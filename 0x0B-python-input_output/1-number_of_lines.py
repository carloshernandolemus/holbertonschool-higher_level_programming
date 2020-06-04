#!/usr/bin/python3
"""Function that returns the numbers of lines"""


def number_of_lines(filename=""):
    """n_lines function"""
    n_lines = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            n_lines += 1
    return(n_lines)
