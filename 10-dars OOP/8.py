class PP:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3


    def UKS(self):
        return (( 0.5 * abs(self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2))) + (0.5 * abs(self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2))))
    
    
    def __str__(self):
        return f"Ular kesishgan joyidagi yuz: {self.UKS()}"
    
o = PP(1,4,5,6,7,8)
print(o)