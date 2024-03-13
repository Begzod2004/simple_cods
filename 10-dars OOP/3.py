class AUS:
    def __init__(self, r):
        self.r = r

    def S(self):
        return 3.14 * (self.r ** 2)
    
    def U(self):
        return 2*3.14*self.r
    
    def __str__(self):
        return f"Aylananing uzunligi: {self.U()}, Doiraning yuzi: {self.S()}"
    
aus = AUS(5)
print(aus)