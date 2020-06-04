#!/usr/bin/python3
"""Function Write"""


def write_file(filename="", text=""):
    """Def function write"""
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
