import unittest
from src.Exceptions.invalid_person import InvalidPersonType
from src.Exceptions.user_exist import UserAlreadyExist
from src.dojo import Dojo


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_dojo_initially_has_no_person(self):
        self.assertEqual(0, len(self.dojo.list_of_staffs)
                         + len(self.dojo.list_of_fellows))

    def test_add_person_adds_to_appropriate_container(self):
        self.dojo.create_room("Makuti", "LivingSpace")
        self.dojo.add_person("Esir", "Fellow", "101", "Y")
        self.dojo.add_person("King'ori", "Staff", "11")
        self.assertEqual(len(self.dojo.list_of_fellows), 1)
        self.assertEqual(len(self.dojo.list_of_staffs), 1)

    def test_person_with_same_id_raises_user_exists_exception(self):
        self.dojo.create_room("Makutile", "LivingSpace")
        with self.assertRaises(UserAlreadyExist):
            self.dojo.add_person("Wanjira", "Fellow", "999")
            self.dojo.add_person("Ngaruiya", "Fellow", "999", "Y")

    def test_invalid_person_type_raises_invalid_type_exception(self):
        with self.assertRaises(InvalidPersonType, msg="Invalid Person Type"):
            self.dojo.add_person("Kamaku", "Security", "030")

if __name__ == '__main__':
    unittest.main()
