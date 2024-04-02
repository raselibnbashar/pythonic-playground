class Student:
    roll = ""
    gpa = ""

    #def set_value(self,roll,gpa):
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

meghla = Student(202,3.32)
#meghla.set_value(202,3.32)
meghla.display()


subarna = Student(201,2.32)
#subarna.set_value(201,2.32)
subarna.display()

