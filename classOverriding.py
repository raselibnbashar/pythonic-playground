class Phone:
    def __init__(self):
        print("Phone class")



class iPhone(Phone):
    def __init__(self):
        super().__init__()
        print("iPhone Class")

i = iPhone()



