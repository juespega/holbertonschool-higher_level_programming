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


if __name__ == '__main__':
    unittest.main()