import unittest
from models.base import Base

class TestBase(unittest.TestCase):
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

    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        # The result should be an empty JSON string ("[]")
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        # The result should be an empty JSON string ("[]")
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        result = Base.to_json_string([{'id': 12}])
        # The result should be a JSON string with the dictionary provided
        self.assertEqual(result, '[{"id": 12}]')

    # def test_to_json_string_single_dict_as_string(self):
    #     result = Base.to_json_string([{'id': 12}], returning_string=True)
    #     # The result should be a JSON string with the dictionary provided
    #     self.assertEqual(result, '[{"id": 12}]')

    # def test_from_json_string_none(self):
    #     result = Base.from_json_string(None)
    #     self.assertEqual(result, [])  # El resultado debe ser una lista vacía ([])

    # def test_from_json_string_empty_list(self):
    #     result = Base.from_json_string("[]")
    #     self.assertEqual(result, [])  # El resultado debe ser una lista vacía ([])

    # def test_from_json_string_single_dict(self):
    #     result = Base.from_json_string('[{"id": 89}]')
    #     self.assertEqual(result, [{'id': 89}])  # El resultado debe ser una lista con el diccionario proporcionado

    # def test_from_json_string_single_dict_as_list(self):
    #     result = Base.from_json_string('[{"id": 89}]', returning_list=True)
    #     self.assertEqual(result, [{'id': 89}])  # El resultado debe ser una lista con el diccionario proporcionado



if __name__ == '__main__':
    unittest.main()