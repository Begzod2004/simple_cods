import math
class II:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def uchburchak_yuzi(self):
        return 0.5 * abs(self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2))

    def __str__(self):
        return f"Uchburchak yuzi:{self.uchburchak_yuzi}"



S = II(3, 4, 2, 7, 2, 4)
print(S)
