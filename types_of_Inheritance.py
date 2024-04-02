class A:
    def display1(self):
        print("I am Class A")

class B(A):
    def display2(self):
        print("I am Class B")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am Class C")

p = C()
p.display3()