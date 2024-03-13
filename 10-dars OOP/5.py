class MT:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2 
        self.y1 = y1
        self.y2 = y2

    def D(self):
        return (((self.x2 - self.x1) ** 2)+((self.y2 - self.y1) ** 2) ** 0.5)
    
    def __str__(self):
        return f"Ular orasidagi masofa: {self.D()}."
    
son = MT(5, 6, 7, 8)
print(son)