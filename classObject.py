class Student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

meghla = Student()
meghla.roll = 111
meghla.gpa = 4.34
meghla.display()


subarna = Student()
subarna.roll = 112
subarna.gpa = 4.24
meghla.display()
#print(isinstance(meghla,Student))
