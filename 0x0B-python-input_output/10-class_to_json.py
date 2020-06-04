#!/usr/bin/python3
"""Def class json"""


def class_to_json(obj):
    """Class function"""
    tx = {}
    if hasattr(obj, "__dict__"):
        tx = obj.__dict__.copy()
    return(tx)
