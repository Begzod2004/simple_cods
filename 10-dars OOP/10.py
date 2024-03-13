class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y


obj = MyClass(3, 4)
print("Yigindisi:", obj.add())    
print("Kop:", obj.multiply())   
