#!/usr/bin/python3
"""Def an attribute function"""


def add_attribute(obj, name, value):
    """Function thar returns if is true or false"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
