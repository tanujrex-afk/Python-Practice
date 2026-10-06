class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("vehicle is moving")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail")
car1=Car("Toyota","Hilux")
boat1=Boat("Eternal","E80")        
for vehicel in (car1,boat1):
        print(vehicel.brand)
        print(vehicel.model)
        vehicel.move()
