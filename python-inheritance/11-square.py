#!/usr/bin/python3
"""
Crating empty class BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry class definition
    """

    def area(self):
        """
        Raise an exception indicating that
        the area() method is not implemented.

        Raises:
            Exception: Indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
