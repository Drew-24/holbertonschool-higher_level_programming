#!/usr/bin/python3
""" Module holds class that inherits from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class inherits from Rectangle """

    def __init__(self, size):
        """ instantation """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
