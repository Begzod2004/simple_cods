a = int(input("a = "))
b = int(input("b = "))
k = 1
sum = 0
for i in range(a+1,b):
  k = i * i
  sum = sum + k
print(sum)