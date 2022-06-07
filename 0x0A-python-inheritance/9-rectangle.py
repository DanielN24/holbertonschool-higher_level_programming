#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ raises an Exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate if it is a integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ class Rectangle that defines a rectangle """

    def __init__(self, width, height):
        """ initialize a Rectangle
        args1: width = width of Rectangle
        args2: height = height of Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the Rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
