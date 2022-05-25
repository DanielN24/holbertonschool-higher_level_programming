#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """this class represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square
        args:
            size = size of square
            position = position of square"""
        self.size = size
        self.position = position

    @property   # Getter
    def size(self):
        """get the size of the square"""
        return (self.__size)

    @property
    def position(self):
        """get the position of the square"""
        return (self.__position)

    @size.setter  # Setter
    def size(self, value):
        """set and validate the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(tuple) != 2 or
                not all(num >= 0 for num in value) or
                not all(isinstance(num, int)for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for j in range(self.__size)]))
