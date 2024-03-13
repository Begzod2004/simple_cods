a = int(input("Son kiriting:"))
b = int(input("Son kiriting:"))
c = int(input("Son kiriting:"))
if a>0 and b>0 and c>0:
  print("3ta musbat")
elif (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
  print("2ta musbat 1ta manfiy")
elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
  print("1ta musbat 2ta manfiy")
elif a<0 and b<0 and c<0:
  print("3ta manfiy")
else:
  print("0")