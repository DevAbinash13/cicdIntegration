class shape:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return (2* self.length)+(2*self.breadth)
    
class rectangle(shape):
    def __init__(self,x,y):
        super().__init__(x,y)

o = rectangle(5,3)
print(o.area())