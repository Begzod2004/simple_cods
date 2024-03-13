x1 = int(input("X1 soni kiriting - "))
x2 = int(input("X2 soni kiriting - "))
y1 = int(input("Y1 soni kiriting - "))
y2 = int(input("Y2 soni kiriting - "))
d = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) ** 0.5

#Geron formulasi
u1 = int(input("Uchburchakni A uchuni kiriting - "))
u2 = int(input("Uchburchakni B uchuni kiriting - "))
u3 = int(input("Uchburchakni C uchuni kiriting - "))
P = u1+u2+u3
s = (u1+u2+u3)/2
S = s*(s-u1)*(s-u2)*(s-u3)
print("Ikki nuqta orasidagi masofa - ",d ,"Parametori - ",P ,"Yuzi - ",S)