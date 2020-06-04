#!/usr/bin/python3
"""Create a class"""


class Student:
    """Function init"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """def function"""
    def to_json(self):
        return(self.__dict__.copy())
