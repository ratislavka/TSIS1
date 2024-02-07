from shape_2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        self.area = self.length * self.width
        return self.area
