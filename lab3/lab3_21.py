
class RectangleShape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
n=int(input())
for i in range(n):
   x=int(input())
   y=int(input())
   rectangle = RectangleShape(x, y)
   print("Area of the rectangle: ", rectangle.area())
