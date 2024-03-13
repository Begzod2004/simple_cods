def ish():
  list = []
  if 0<b<10 and a>10:
    while a>=1:
      c = a%b
      a = a // b
      list.append(c)
    print(list[::-1])
  else:
    print("Noto'g'ri raqam kiritdingiz!")



a = int(input("10lik son kiriting: "))
b = int(input("Sanoq sistemasini kiriting: "))