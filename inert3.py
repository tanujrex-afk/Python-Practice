class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
student1=Student("Alice",24)
print("student name:",student1.name)
print("Student Age:",student1.age)
