#!/usr/bin/python3
"""This is the square class"""


class Square:
    """A class that define the size"""
    def __init__(self, size=0):
        """Initialize the size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
