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
        # Call the constructor of the base class and pass the "id" parameter
        super().__init__(id)
        # Private variable to store the width
        self.__width = width
        # Private variable to store the height
        self.__height = height
        # Private variable to store the x position
        self.__x = x
        # Private variable to store the y position
        self.__y = y

    # Getter for the "width" property
    @property
    def width(self):
        return self.__width

    # Setter for the "width" property
    @width.setter
    def width(self, value):
        self.__width = value

    # Getter for the "height" property
    @property
    def height(self):
        return self.__height

    # Setter for the "height" property
    @height.setter
    def height(self, value):
        self.__height = value

    # Getter for the "x" property
    @property
    def x(self):
        return self.__x

    # Setter for the "x" property
    @x.setter
    def x(self, value):
        self.__x = value

    # Getter for the "y" property
    @property
    def y(self):
        return self.__y

    # Setter for the "y" property
    @y.setter
    def y(self, value):
        self.__y = value
