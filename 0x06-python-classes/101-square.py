#!/usr/bin/python3
"101-square.py define"


class Square:
    """class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Inizialitation of variables
        Arg self identificador
        size tamañe of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Inizialitation of variables
        Arg self identificador
        value of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise value("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Inizialitation of variables
        Arg self identificador
        value of square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size ** 2

    def my_print(self):
        """Inizialitation of variables
        Arg self identificador
        """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
