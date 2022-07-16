"""
Polygon Area Calculator
"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        width = self.width
        height = self.height
        str = ''
        if self.height <= 50 and self.width <= 50:
            for i in range(height):
                for j in range(width):
                    str += "".join("*")
                str += "".join("\n")
        else:
            print("Too big for picture.")
        return str

    def get_amount_inside(self, shape):
        height = shape.height
        width = shape.width
        max_shape = width * height
        max_self = self.width * self.height
        result = max_self / max_shape
        return result

    def aux(self):
        return self.width, self.width

class Square(Rectangle):

    def __init__(self, num):
        self.width = num
        self.height = num


    def __str__(self):
        return f'Square(side={str(self.width)})'

    def set_side(self, num):
        self.width = num
        self.height = num

    def aux(self):
        return self.width
