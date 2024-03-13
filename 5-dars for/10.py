n = int(input("n (n>0) ni kiriting: "))

a = 0
for i in range(1, n + 1):
    if i % 2 == 1:  
        a += 1
    else:  
        a -= 1

print("Javobi -", a)
