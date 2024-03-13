a = float(input("Son kiriting:"))
b = float(input("Son kiriting:"))
if a>b:
  a,b = b,a
  print("a =",a,"b =",b)
else:
  print(a,b)