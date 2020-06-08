#!/usr/bin/python3
"""Create a rectangle class thats inherits from base"""


from models.base import Base
""" import module """


class Rectangle(Base):
    """ class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
