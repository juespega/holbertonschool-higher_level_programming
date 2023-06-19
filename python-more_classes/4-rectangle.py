#!/usr/bin/python3
"""
This module contains an empty class Rectangle that defines a rectangle:"
"""


class Rectangle:
    """
    A class that represents a rectangle.

    Attributes:
        _width (int): The width of the rectangle.
        _height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object.

        Args:
            width (int, optional): The width of the rectangle.
            Defaults to 0.
            height (int, optional): The height of the rectangle.
            Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        If the width or height is equal to 0, it returns an empty string.
        Otherwise, it constructs a string representation of the rectangle
        using the character '#'.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate a new instance.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
