x1 = int(input("X1 soni kiriting - "))
x2 = int(input("X2 soni kiriting - "))
y1 = int(input("Y1 soni kiriting - "))
y2 = int(input("Y2 soni kiriting - "))
t1 = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) ** 0.5
t2 = x2-x1
p = 2*(t1+t2)
S = t1*t2
print("Uning peremetori - ",p,"Yuzasi - ",S)