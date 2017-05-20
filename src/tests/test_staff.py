import unittest

from src.persons import Staff


class TestStaff(unittest.TestCase):
    def setUp(self):
        self.Kimani = Staff("Kimani", "001")

    def test_staff_created(self):
        self.assertEqual("Staff", self.Kimani.person_type)

if __name__ == '__main__':
    unittest.main()
