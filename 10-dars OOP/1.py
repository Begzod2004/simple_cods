
class Canc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def qosh(self):
        return self.x + self.y
    
    def ayirma(self):
        return self.x - self.y
    
    def kop(self):
        return self.x * self.y
    
    def bolinma(self):
        return self.x / self.y

    def __str__(self):
        return f"Raqamlar yig'indisi - {self.qosh()}, Airmasi - {self.ayirma()}, Ko'paytmasi - {self.kop()}, Bolinmasi - {self.bolinma()}"


ob1 = Canc(4, 2)
print(ob1)
