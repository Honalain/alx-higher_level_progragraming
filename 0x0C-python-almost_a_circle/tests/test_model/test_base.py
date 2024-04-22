import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_increment_id(self):
        """ Test that id increment correctly"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id (self):
        """ Test for custom id """
        obj3 = base(id = 10)
        self.assertEqual(obj3.id, 10)

    def test_no_id(self):
        """ Test if there is no id provided """

        obj4 = base()
        self.assertEqual(obj4.id, 3)

if __name == '__main__':
    unittest.main()
