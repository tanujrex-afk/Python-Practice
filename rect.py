class rect:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
rect1=rect(10,5)
print(rect1.area())
        