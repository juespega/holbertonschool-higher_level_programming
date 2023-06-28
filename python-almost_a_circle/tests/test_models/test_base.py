import unittest
from models.base import Base

def test_base_auto_id(self):
    base1 = Base()
    base2 = Base()
    # The first object must have ID 1
    self.assertEqual(base1.id, 1)
    # The second object must have ID 2
    self.assertEqual(base2.id, 2)

def test_base_auto_increment_id(self):
    base1 = Base()
    base2 = Base()
    base3 = Base()
    # The third object must have ID equal to the second plus 1
    self.assertEqual(base3.id, base2.id + 1)

def test_base_custom_id(self):
    base = Base(89)
    # The object must have the custom ID (89)
    self.assertEqual(base.id, 89)









if __name__ == '__main__':
    unittest.main()