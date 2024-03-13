n = int(input("n kiriting: "))

k = n // 3  
if n % 3 == 0:  
    k -= 1

while 3 * k >= n:
    k -= 1

print("Eng katta k butun son:", k)
