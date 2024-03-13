a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a>b and b>c or c>b and b>a:
  print(b)
elif a>c and c>b or b>c and c>a:
  print(c)
elif b>a and a>c or c>a and a>b:
  print(a)
else:
  print("Barchasi teng")