#!/usr/bin/python3
"""module of 'Rectangle' class"""

from .base import Base


class Rectangle(Base):
    """Representation of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width
    
    @property
    def height(self):
        """height getter method"""
        return self.__height
    
    @property
    def x(self):
        """x getter method"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """x setter method"""
        self.__x = value
    
    @property
    def y(self):
        """y getter method"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """y setter method"""
        self.__y = value