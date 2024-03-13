a = int(input("Son kiriting:"))
b = int(input("Son kiriting:"))
if a>b:
  b = a
  print("a =",a,"b =",b)
elif b>a:
  a = b
  print("a =",a,"b =",b)
else:
  a = 0
  b = 0
  print("a =",a,"b =",b)
