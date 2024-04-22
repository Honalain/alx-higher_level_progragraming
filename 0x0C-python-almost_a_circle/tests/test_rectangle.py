import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.Testcase):
    """ Test case for the Rectangle clas. s"""
    
    def test_constructor(self):
        """Test cases for the rectangle class."""
        r = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertequal(r.id, 100)

    def test_width(self):
        """ Test width attribute. """
        r = Rectangle(5, 10)
        r.width = 7
        self.assertEqual(r.width,7)

        with self.assertRaises(TypeError):
            r.width = "invalid"

        with self.assertRaises(ValueError):
            r.width = 0


    def test_height(self):
        """Test height attribute. """
        r = Rectanngle(5, 10)
        r.height =  15
        self.assertEqual(r.height, 15)


        with self.assertRaises(TypeError):
            r.height = "invalid"

        with self.assertRaises(ValueError):
            r.height = 0
    
    def test_x(self):
        """Test x attribute. """
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)

        with self.assertRaises(TypeError):
            r.x = "invalid"


    def test_y(self):
        """Test y attribute. """
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)

        with self.assertRaises(TypeError):
            r.y = "invalid"


if __name__ == '__main___':
    unittest.main()
