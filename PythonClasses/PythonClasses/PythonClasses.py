from math import pi
class Rectangle:
    def __init__(self, width, height): 
        self.rArea = width * height
    def pArea(self):
        print("The area of a Rectangle is ",self.rArea)
class Triangle:
    def __init__(self, width, base): 
        self.tArea = width * base/2
    def pArea(self):
        print("The area of a Triangle is ",self.tArea)
class Square:
    def __init__(self, side): 
        self.sArea = pow(side, 2)
        self.bArea = 6*(pow(side,2))
    def pArea(self):
        print("The area of a Square is ", self.sArea)
        print("The area of a Cube is ", self.bArea)
class Circle:
    def __init__(self, radius): 
        self.cArea = round( (pi*pow(radius,2)),2)
        self.sArea = round( (4*(pi*pow(radius,2))),2)
    def pArea(self):
        print("The area of a Circle is ",self.cArea)
        print("The area of a Sphere is ",self.sArea)

def main():
    # enter retangle
    r1 = Rectangle(4, 5)
    # print rectangle
    r1.pArea()

    # enter Triangle
    r1 = Triangle(4, 5)
    # print rectangle
    r1.pArea()

    # enter Square
    r1 = Square(5)
    # print rectangle
    r1.pArea()

    # enter Square
    r1 = Circle(5)
    # print rectangle
    r1.pArea()
main()