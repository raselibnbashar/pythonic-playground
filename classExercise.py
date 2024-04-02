class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 *  self.base * self.height
        print("Area =",area)

v1 = Triangle(10,20)
v1.calculate_area()
v2 = Triangle(20,30)
v2.calculate_area()

