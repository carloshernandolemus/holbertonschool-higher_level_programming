#!/usr/bin/python3
"""Def a class"""


class MyInt(int):
    """Def eq function"""
    def __eq__(self, other):
        return(int.__ne__(self, other))
    """Def ne function"""
    def __ne__(self, other):
        return(int.__eq__(self, other))
