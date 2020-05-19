#!/usr/bin/python3
"""This is the squere class"""


class Square:
    """This part define the size"""

    def __init__(self, size=0):
        """The size private attribute"""

        if type(size) != int:
            raise TypeError('size must be a integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._size = size
