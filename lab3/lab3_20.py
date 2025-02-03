
class Shape:
    def __init__(self):
        self.area = 0

    def calculate_area(self):
        return self.area

    def print_area(self):
        print("Area of the shape: " ,self.area)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def calculate_area(self):
        self.area = self.length * self.length
        return self.area

    def print_area(self):
        print("Area of the square:", self.calculate_area())
shape = Shape()
shape.print_area()

square = Square(9)
square.print_area()
