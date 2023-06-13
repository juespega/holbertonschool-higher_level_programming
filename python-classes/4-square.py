#!/usr/bin/python3
"""Creating the square class whit Private instance attribute: size"""


class Square:

    def __init__(self, size=0):
        """Square class definition and Instantiation with size optional size"""
        self.size = size

    @property
    def size(self):
        """allows to get the value of size and returns self.__size"""
        return self.__size

    @size.setter
    def size(self, value):
        """allows assigning a value to size and performs type and value vali"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
