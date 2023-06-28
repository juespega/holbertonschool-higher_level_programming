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
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        """
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        """
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        Getter method for the x-coordinate attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate attribute.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """
        Getter method for the y-coordinate attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate attribute.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

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
