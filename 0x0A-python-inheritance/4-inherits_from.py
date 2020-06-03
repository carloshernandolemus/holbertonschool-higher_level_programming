#!/usr/bin/python3
"""Def the function prototype"""


def inherits_from(obj, a_class):
    """Conditional class"""
    if type(obj) is a_class:
        return(False)
    return(isinstance(obj, a_class))
