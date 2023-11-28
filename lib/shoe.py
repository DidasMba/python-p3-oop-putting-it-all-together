#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "New"

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            print("size must be an integer")
            return
        self._size = new_size

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"



