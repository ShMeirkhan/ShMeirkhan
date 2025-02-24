import math

def trapezoid_area(height, base1, base2):
    return math.fabs(height * (base1 + base2) / 2)

height = int(input())
base1 = int(input())
base2 = int(input())
area = trapezoid_area(height, base1, base2)
print("The area of the trapezoid is:", area)