a = int(input("Sonni kiriting:"))
b = a%10
c = a%100//10
d = a//100
e = b==c or b==d or c==d
print(e)