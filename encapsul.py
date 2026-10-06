class Person:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
p1=Person("Jerry",56000)
print(p1.name)
print(p1.get_salary())