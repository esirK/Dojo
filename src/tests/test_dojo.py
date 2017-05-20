import unittest

from src.Exceptions.invalid_person import InvalidPersonType
from src.dojo import Dojo


class TestDojo(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_dojo_is_initially_empty(self):
        self.assertEqual(0, len(self.dojo.list_of_staffs)
                         + len(self.dojo.list_of_fellows))

    def test_add_person_adds_to_appropriate_container(self):
        self.dojo.add_person("Esir", "Fellow", "101", "Y")
        self.dojo.add_person("King'ori", "Staff", "11")
        self.assertEqual(len(self.dojo.list_of_fellows), 1)
        self.assertEqual(len(self.dojo.list_of_staffs), 1)

    def test_person_with_same_id_not_added(self):
        self.dojo.add_person("Ngaruiya", "Fellow", "001", "Y")

    def test_invalid_person_type_raises_invalid_type_exception(self):
        with self.assertRaises(InvalidPersonType, msg="Invalid Person Type"):
            self.dojo.add_person("Kamaku", "Security", "030")


if __name__ == '__main__':
    unittest.main()
