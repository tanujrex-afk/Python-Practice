class Dog:
    def cry(self):
        print("Boww")
class Cat:
    def cry(self):
        print("Meow")
class Cow:
    def cry(self):
        print("Mooo")
dog1=Dog()
cat1=Cat()
cow1=Cow()
for animals in(dog1,cat1,cow1):
    animals.cry()
