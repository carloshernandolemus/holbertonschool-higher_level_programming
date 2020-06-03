#!/usr/bin/python3
"""Def class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Def init function"""
    def __init__(self, width, height):
        """Inicialized inhereit"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """Def an area function"""
    def area(self):
        return self.__width * self.__height
    """Def str function"""
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
