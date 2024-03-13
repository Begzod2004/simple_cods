n = int(input("n kiriting: "))
a = 1

while n > 0:
    if n % 2 == 1:
        a *= n
    else: 
        a *= 2
    n -= 2

print("n ikki factorial:", a)
