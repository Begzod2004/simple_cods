class T1:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def s(self):
        return (self.x ** 2)+(self.y ** 2)
    
    def p(self):
        return self.x + self.y + self.z
    
    def __str__(self):
        return f"Yuzasi: {self.s()}, Parametori: {self.p()}"

car1 = T1(1, 4, 6)
print(car1)        




