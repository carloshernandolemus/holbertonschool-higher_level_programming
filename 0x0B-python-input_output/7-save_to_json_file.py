#!/usr/bin/python3
"""Import json module"""


import json


def save_to_json_file(my_obj, filename):
    """Open a save function def"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
