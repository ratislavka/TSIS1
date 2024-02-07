class Shape:
    def __init__(self):
        self.area = 0

    def compute_area(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def compute_area(self):
        self.area = self.length * self.length
        return self.area