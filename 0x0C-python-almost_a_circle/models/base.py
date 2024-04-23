#!/usr/bin/python3

"""
Base: class to manage id of attribute to avoid duplicating the same code

"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
