import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_with_width_and_height(self):
        rectangle = Rectangle(1, 2)
        # Check that the width is equal to 1
        self.assertEqual(rectangle.width, 1)
        # Check that the height is equal to 2
        self.assertEqual(rectangle.height, 2)
        # Check that the position x is equal to 0
        self.assertEqual(rectangle.x, 0)
        # Check that the position y is equal to 0
        self.assertEqual(rectangle.y, 0)

    def test_rectangle_with_width_height_and_x(self):
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 0)

    def test_rectangle_with_width_height_x_and_y(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_with_width_height_x_y_and_id(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 5)

    def test_rectangle_with_invalid_width_str(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_with_invalid_height_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_with_invalid_x_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_with_invalid_y_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
    
    def test_rectangle_with_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_with_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_with_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_with_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_with_invalid_width_0_and_height(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_with_invalid_width_and_height_0(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_area_calculation(self):
        rectangle = Rectangle(3, 4)
        area = rectangle.area()
        # Check that the area calculation is correct
        self.assertEqual(area, 12)

    def test_str_method(self):
        """
        Test the __str__() method of Rectangle.
        """
        rectangle = Rectangle(1, 2, 3, 4, 5)
        string_representation = str(rectangle)
        expected_output = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(string_representation, expected_output)

    # def test_display_without_x_and_y(self):
    #     """
    #     Test the display() method of Rectangle without x and y offsets.
    #     """
    #     rectangle = Rectangle(2, 3)
    #     expected_output = "##\n##\n##\n"
    #     self.assertEqual(rectangle.display(), expected_output)

    # def test_display_without_y(self):
    #     """
    #     Test the display() method of Rectangle without y offset.
    #     """
    #     rectangle = Rectangle(2, 3, 1)
    #     expected_output = " ##\n ##\n ##\n"
    #     self.assertEqual(rectangle.display(), expected_output)

    # def test_display(self):
    #     """
    #     Test the display() method of Rectangle.
    #     """
    #     rectangle = Rectangle(2, 3, 1, 2)
    #     expected_output = "\n\n ##\n ##\n ##\n"
    #     self.assertEqual(rectangle.display(), expected_output)

    # def test_to_dictionary(self):
    #     """
    #     Test the to_dictionary() method of Rectangle.
    #     """
    #     rectangle = Rectangle(1, 2, 3, 4, 5)
    #     expected_output = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
    #     self.assertEqual(rectangle.to_dictionary(), expected_output)

    # def test_update_method(self):
    #     """
    #     Test the update() method of Rectangle.
    #     """
    #     rectangle = Rectangle(1, 2, 3, 4, 5)
    #     rectangle.update(6, 7, 8, 9, 10)
    #     self.assertEqual(rectangle.id, 6)
    #     self.assertEqual(rectangle.width, 7)
    #     self.assertEqual(rectangle.height, 8)
    #     self.assertEqual(rectangle.x, 9)
    #     self.assertEqual(rectangle.y, 10)

    # def test_update_method_with_id_only(self):
    #     """
    #     Test the update() method of Rectangle with only the id parameter.
    #     """
    #     rectangle = Rectangle(1, 2, 3, 4, 5)
    #     rectangle.update(6)
    #     self.assertEqual(rectangle.id, 6)
    #     self.assertEqual(rectangle.width, 1)
    #     self.assertEqual(rectangle.height, 2)
    #     self.assertEqual(rectangle.x, 3)
    #     self.assertEqual(rectangle.y, 4)

    # def test_update_method_with_id_and_width(self):
    #     """
    #     Test the update() method of Rectangle with id and width parameters.
    #     """
    #     rectangle = Rectangle(1, 2, 3, 4, 5)
    #     rectangle.update(6, 7)
    #     self.assertEqual(rectangle.id, 6)
    #     self.assertEqual(rectangle.width, 7)
    #     self.assertEqual(rectangle.height, 2)
    #     self.assertEqual(rectangle.x, 3)
    #     self.assertEqual(rectangle.y, 4)

    # def test_update_method_with_id_width_and_height(self):
    #     """
    #     Test the update() method of Rectangle with id, width, and height parameters.
    #     """
    #     rectangle = Rectangle(1, 2, 3, 4, 5)
    #     rectangle.update(6, 7,


if __name__ == '__main__':
    unittest.main()