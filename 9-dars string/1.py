s = input("So'zni kiriting:")
n = int(input("Sonni kiriting:"))
if len(s)<n:
  a = n - len(s)
  b = '.'
  c = a*b
  print(s+c)
else:
  print(s[:n])