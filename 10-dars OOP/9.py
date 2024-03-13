class ABC:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Qoshish(self):
        return self.a + self.b + self.c
    
    def Kopaytmasi(self):
        return self.a * self.b * self.c
    
    def __str__(self):
        f"Yigindisi: {self.Qoshish()}, Kopaytmasi: {self.Kopaytmasi()}"

i = int(input("A son kiriting: "))
o = int(input("B son kiriting: "))
p = int(input("C son kiriting: "))
v = ABC(i, o, p)
print(v)

