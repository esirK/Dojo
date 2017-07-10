import unittest

from src.Exceptions.room_exceptions import OfficeFull, LivingSpaceFull
from src.dojo import Dojo
from src.persons import Fellow
from src.rooms import LivingSpace, Office


class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def __fill_room(self, room_name, room_type, size):
        self.office = Office(room_name)
        self.lv_room = LivingSpace(room_name)
        for person in range(0, size):
            if room_type.lower() == "livingspace":
                self.lv_room.add_fellow((Fellow("Person" + str(person), str(person), "Y")))
            elif room_type.lower() == "office":
                # since we are testing if an office is full, any person_type can be used
                self.office.add_person(Fellow("Person" + str(person), str(person), "Y"))

    def test_room_is_successfully_created(self):
        init_len = len(self.dojo.list_of_offices)
        self.dojo.create_room("Makuti", "Office")
        self.dojo.create_room("Texas", "LivingSpace")
        new_len = len(self.dojo.list_of_offices)
        self.assertEqual(1, new_len - init_len)
        self.assertEqual(1, len(self.dojo.list_of_living_space))

    def test_office_occupies_six_people(self):
        self.__fill_room("Mwathi", "Office", 6)
        with self.assertRaises(OfficeFull):
            self.office.add_person(Fellow("Isaiah Kimotho", "0900", "Y"))

    def test_lv_room_occupies_four_fellows(self):
        self.__fill_room("Mwathini", "LivingSpace", 4)
        with self.assertRaises(LivingSpaceFull):
            self.lv_room.add_fellow((Fellow("Isaiah Kimotho", "0900", "Y")))

if __name__ == '__main__':
    unittest.main()
