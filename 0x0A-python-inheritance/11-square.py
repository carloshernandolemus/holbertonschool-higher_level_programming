#!/usr/bin/python3
"""Def class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Def init"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
    """Def square area"""
    def area(self):
        return(super().area())
    """Def str"""
    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
