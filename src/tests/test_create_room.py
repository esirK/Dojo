import unittest

from src.dojo import Dojo


class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_room_is_successfully_created(self):
        init_len = len(self.dojo.list_of_offices)
        self.dojo.create_room("Makuti", "Office")
        self.dojo.create_room("Texas", "LivingSpace")
        new_len = len(self.dojo.list_of_offices)
        self.assertEqual(1, new_len-init_len)
        self.assertEqual(1, len(self.dojo.list_of_living_space))

if __name__ == '__main__':
    unittest.main()
