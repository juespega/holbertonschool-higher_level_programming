#!/usr/bin/python3
"""
Crating empty class BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize a Square object with the size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size * self.__size
