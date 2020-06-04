#!/usr/bin/python3
"""Import json module"""


import json


def load_from_json_file(filename):
    """Def function that load from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return(json.load(f))
