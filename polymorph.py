class Car:
    def move(self):
        print("Drive!")
class Boat:
    def move(self):
        print("Sail")
class Plane:
        def move(self):
             print("Fly")
car1=Car()
boat1=Boat()
plane1=Plane()

for vehicle in (car1,boat1,plane1):
     vehicle.move()
