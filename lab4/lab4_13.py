import math
def area(base,height):
    return math.fabs(base*height)
base = int(input())
height =int(input())
solution=area(base,height)
print(f"The area of the parallelogram is: {solution}")