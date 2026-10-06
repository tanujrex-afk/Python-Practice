class people:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=people("John","doe")
x.printname()
class Student(people):
    pass