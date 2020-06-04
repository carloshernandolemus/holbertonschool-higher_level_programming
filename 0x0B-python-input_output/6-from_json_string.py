#!/usr/bin/python3
"""Loads file"""


import json


def from_json_string(my_str):
    """Returns load function"""
    return(json.loads(my_str))
