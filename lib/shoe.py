#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        print("The shoe has been repaired.")
        self.condition = "New"
