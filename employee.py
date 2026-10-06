class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
e1=employee("Aron",567,20000)
e2=employee("Vishal",980,40000)
print(e1.name,e1.id,e1.salary)
print(e2.name,e2.id,e2.salary)
del e1
print(e1)