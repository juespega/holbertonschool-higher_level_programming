#!/usr/bin/python3
"""
Crate a Rectangle class inheriting from the Base class
"""
# Import the Base class from the "base" module
from models.base import Base


class Rectangle(Base):
    """
    Class representing a rectangle and inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of the Rectangle class
        """
        """Call the constructor of the base class and pass
        the "id" parameter (2)"""
        super().__init__(id)

        # Private variable to store the width (2)
        # Call the width setter to validate and assign the value (3)
        self.width = width

        # Private variable to store the height (2)
        # Call the height setter to validate and assign the value (3)
        self.height = height

        # Private variable to store the x position (2)
        # Call the x setter to validate and assign the value (3)
        self.x = x

        # Private variable to store the y position (2)
        # Call the y setter to validate and assign the value (3)
        self.y = y

    # Getter for the "width" property (2)
    @property
    def width(self):
        return self.__width

    # Setter for the "width" property (2)
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("width must be an integer")
        if value <= 0:
            # Raise ValueError if value is not greater than 0 (3)
            raise ValueError("width must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__width = value

    # Getter for the "height" property (2)
    @property
    def height(self):
        return self.__height

    # Setter for the "height" property (2)
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("height must be an integer")
        if value <= 0:
            # Raise ValueError if value is not greater than 0 (3)
            raise ValueError("height must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__height = value

    # Getter for the "x" property (2)
    @property
    def x(self):
        return self.__x

    # Setter for the "x" property (2)
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("x must be an integer")
        if value < 0:
            # Raise ValueError if value is not greater than or equal to 0 (3)
            raise ValueError("x must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__x = value

    # Getter for the "y" property (2)
    @property
    def y(self):
        return self.__y

    # Setter for the "y" property (2)
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("y must be an integer")
        if value < 0:
            # Raise ValueError if value is not greater than or equal to 0 (3)
            raise ValueError("y must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__y = value
