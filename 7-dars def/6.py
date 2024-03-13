def ish():
  list = []
  while a>=1:
    b = a%2
    a = a // 2
    list.append(b)
  print(list[::-1])

a = int(input("Son kiriting: "))