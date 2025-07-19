class circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        print("AREA OF CIRCLE")
        print("Area of circle: ",3.14*self.radius**2)
    def perimeter(self):
        print("PERIMETER OF CIRCLE")
        print("Perimeter of circle: ",2*3.14*self.radius)
    def details(self):
        print("----------------------")
        print("CIRCLE DETAILS")
        print("Radius: ",self.radius)
        print("----------------------")

class triangle:
    def __init__(self, side1, side2, side3,base,height):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.base=base
        self.height=height
    def area(self):
        print("AREA OF TRIANGLE")
        area=(self.base*self.height)//2
        print("Area of triangle: ",area)
    def perimeter(self):
        print("PERIMETER OF TRIANGLE")
        peri=self.side1+self.side2+self.side3
        print("Perimeter of triangle: ",peri)
    def details(self):
        print("----------------------")
        print("TRIANGLE DETAILS")
        print("Side1: ",self.side1)
        print("Side2: ",self.side2)
        print("Side3: ",self.side3)
        print("Base: ",self.base)
        print("Height: ",self.height)
        print("----------------------")


class rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("AREA OF RECTANGLE")
        area=self.length*self.breadth
        print("Area of rectangle: ",area)
    def perimeter(self):
        print("PERIMETER OF RECTANGLE")
        peri=2*(self.length+self.breadth)
        print("Perimeter of rectangle: ",peri)
    def details(self):
        print("----------------------")
        print("RECTANGLE DETAILS")
        print("Length: ",self.length)
        print("Breadth: ",self.breadth)
        print("----------------------")

r1=rectangle(3,7)
r1.details()
print("\n")
r1.area()
print("\n")
r1.perimeter()
print("\n")
c1=circle(3.4)
c1.details()
print("\n")
c1.area()
print("\n")
c1.perimeter()
print("\n")
t1=triangle(4,7,1,6,5.7)
t1.details()
print("\n")
t1.area()
print("\n")
t1.perimeter()
