#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ raises an Exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        Rectangle class
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        return (self.__width * self.__height)


class Square(Rectangle):
    """ class Square that defines a Square """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the Square area"""

        return self.__size * self.__size
