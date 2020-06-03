#!/usr/bin/python3
"""Def class mylist"""


class MyList(list):
    """DEf function print sorted"""
    def print_sorted(self):
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
