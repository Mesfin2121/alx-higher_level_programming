#!/usr/bin/python3
"6-square.py define"


class Square:
    """class Square
    """
    def __init__(self, size=0):
        """Inizialitation of variables
        Arg self identificador
        size tamañe of square
        """
        self.size = size

    def area(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size ** 2

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
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
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
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
