#!/usr/bin/python3
from models.rectangle import Rectangle

""" A module for square."""


class Square(Rectangle):
    """A Class representing Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a square instance. """
        super().__init__(size, size, x, y)

    def __str__(self):

        """Return a string representatiion of the square. """
        return "[Square] ({}) {}/{}-{}"\
               .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for the size attribute. """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attribute."""
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 4:
                self.x = args[2]
                sefl.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, Value)
