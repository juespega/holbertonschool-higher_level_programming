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
