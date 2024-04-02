class Phone:
    def call(self):
        print("Call list method")

    def message(self):
        print("Message list method")

class iPhone(Phone):
    def voice(self):
        print("Voice list method")

p = Phone()
p.call()
p.message()
#print(issubclass(Phone,iPhone))



