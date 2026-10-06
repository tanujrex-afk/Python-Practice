class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal is barking")
class Dog(animal):
    def eat(self):
        print("dog is eating")
d=Dog("Baxter")
d.speak()
d.eat()