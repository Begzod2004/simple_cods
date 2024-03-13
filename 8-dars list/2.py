def powers_of_two(n):
    if n <= 0:
        return "n o'zgaruvchisi musbat va 0 dan katta bo'lishi kerak"
    
    powers = [] 

    for i in range(n):
        powers.append(2 ** i)

    return powers

n = int(input("n ni kiriting (n>0): "))
result = powers_of_two(n)
print(f"{n} o'lchamli massiv: {result}")
