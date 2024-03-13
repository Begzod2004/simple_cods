class R:
    def __init__(self, S):
        self.S = S

    def rt(self):
        return ((self.S / 3.14) ** 0.5)
    
    def __str__(self):
        return f"Uning radiusi: {self.rt()}."
    

RT = R(int(input("Son kiriting: ")))
print(RT)