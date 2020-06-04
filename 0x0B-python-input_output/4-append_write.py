#!/usr/bin/python3
"""Append function"""


def append_write(filename="", text=""):
    """Def a append function"""
    with open(filename, 'a', encoding="utf-8") as f:
        return(f.write(text))
