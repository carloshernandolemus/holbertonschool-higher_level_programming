#!/usr/bin/python3
"""Create a new class"""


class Base:
    """
        This class will be the “base” of all other classes in
        this project
    """
    __nb_objects = 0
    """ private class attribute """

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
