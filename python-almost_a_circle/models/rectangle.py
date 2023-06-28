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

    @property
    def width(self):
        """Getter for the "width" property (2)"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the "width" property (2)"""
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("width must be an integer")
        if value <= 0:
            # Raise ValueError if value is not greater than 0 (3)
            raise ValueError("width must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__width = value

    @property
    def height(self):
        """Getter for the "height" property (2)"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the "height" property (2)"""
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("height must be an integer")
        if value <= 0:
            # Raise ValueError if value is not greater than 0 (3)
            raise ValueError("height must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__height = value

    @property
    def x(self):
        """Getter for the "x" property (2)"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the "x" property (2)"""
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("x must be an integer")
        if value < 0:
            """Raise ValueError if value is not greater than or
            equal to 0 (3)"""
            raise ValueError("x must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__x = value

    @property
    def y(self):
        """Getter for the "y" property (2)"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the "y" property (2)"""
        if not isinstance(value, int):
            # Raise TypeError if value is not an integer (3)
            raise TypeError("y must be an integer")
        if value < 0:
            """Raise ValueError if value is not greater than or
            equal to 0 (3)"""
            raise ValueError("y must be > 0")
        # Assign the validated value to the private attribute (3)
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle. (4)

        Returns:
            The area of the rectangle."""
        return self.__height * self.__width

    def display(self):
        """
        Print the Rectangle instance with the character '#' (5),
        accounting for x and y offsets (7)
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle using the provided arguments
        or keyword arguments
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance (6)
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}")

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
