n = int(input("n kiriting: "))

k = 1
while k * k <= n:
    k += 1

k -= 1  

print("Kvadrati n dan katta bo'lmagan eng katta butun son:", k)
