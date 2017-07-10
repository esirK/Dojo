import unittest

from src.persons import Fellow


class TestFellows(unittest.TestCase):
    def setUp(self):
        self.Esir = Fellow("Esir Kings", "001")
        self.Akoa = Fellow("Victoria Akoa", "002", "Y")

    def test_fellow_is_created(self):
        self.assertEqual(self.Esir.person_type, "Fellow")

    def test_fellow_not_accommodated_by_default(self):
        self.assertEqual(self.Esir.wants_accommodation, "N")

    def test_fellow_accommodated_on_choice(self):
        self.assertEqual(self.Akoa.wants_accommodation, "Y")

if __name__ == '__main__':
    unittest.main()
