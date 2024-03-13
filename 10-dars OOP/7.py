class OA:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Oa(self):
        return (self.a + self.b)//2
    
    def Go(self):
        return(self.a * self.b) ** 0.5
    
    def __str__(self):
        return f"Arifmetik o'rta: {self.Oa()}, Geometrik o'rta: {self.Go()}"
    
p = OA(5, 7)
print(p)