a = int(input("Son kiriting:"))
b = int(input("Son kiriting:"))
if a==b:
  a=0
  b=0
  print(a,b)
else:
  a = a+b
  b = a
  print(a,b)