#!/usr/bin/python3
class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).

        Returns:
        None
        """
        sorted_list = sorted(self)
        print(sorted_list)
