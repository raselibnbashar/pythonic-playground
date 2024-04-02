from abc import ABC,abstractmethod
class Shape:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        result = 0.5 * self.v1 * self.v2
        print("Triangle area is =",result)

class Rectangle(Shape):
    def area(self):
        result = self.v1 * self.v2
        print("Rectangle area is =",result)


t1 = Triangle(10,20)
t1.area()

t2 = Rectangle(10,20)
t2.area()
