#!/usr/bin/python3
"""
Crate a Square class inheriting from the Rectangle class
"""
# Import the Rectangle class from the "rectangle" module
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from the
    Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            ValueError: If the size value is not greater than 0.
            TypeError: If the size value is not an integer.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square object.

        Args:
            *args: List of arguments in the following order:
            [id, size, x, y]
            **kwargs: Keyworded arguments where each key represents an
            attribute name.

        Raises:
            ValueError: If a size value is not greater than 0.
            TypeError: If a size value is not an integer.
        """
        if args and len(args) > 0:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
