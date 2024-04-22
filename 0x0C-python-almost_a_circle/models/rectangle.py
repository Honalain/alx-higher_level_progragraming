#!/usr/bin/python3

""" Module: class to protect attributes of class, with setter and getter """
from models.base import Base


class Rectangle(Base):

    """ A Class for Rectangle """

    def __init__(self, *args, **kwargs):

        """Initialise a Rectangle instance."""
        super().__init__(**kwargs)
        if len(args) == 5:
            self.width = args[0]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
            self.id = args[4]
        elif len(args) == 4:
            self.width = args[0]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        elif len(args) == 3:
            self.width = args[0]
            self.height = args[1]
            self.x = args[2]
            self.y = 0
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]
            self.x = 0
            self.y = 0
        else:
            raise TypeError("Take 2-4 argument but {} given".format(len(args)))

    @property
    def width(self):
        """ Getter for width atrribute """

        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute """
        if not isinstance(value, int):
            raise TypeError("Width must be an interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height value must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute. """
        return self.__x

    @x.setter
    def x(self, value):

        """ Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        """ Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):

        """ setter for y attribute. """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):

        """ Calculate area of rectangle"""
        return self.width * self.height

    def display(self):

        """Display the rectangle with '#' characters, considering X and y."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print('' * self.x + '#' * self.width)

    def __str__(self):

        """Return string representation of the string. """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
                )

    def update(self, *args):

        """ Assign argument to attributes."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
