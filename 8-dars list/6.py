def MGH(n, a, b):
    if n <= 2:
        return "n 2 dan katta bo'lishi kerak"
    
    massiv = [a, b]  # 1-element a, 2-element b
    
    for i in range(2, n):
        massiv.append(sum(massiv[:i]))  # Har keyingi element oldingi barcha elementlarning yig'indisiga teng
        
    return massiv

n = int(input("n kiriting: "))
a = int(input("a kiriting: "))
b = int(input("b kiriting: "))

natija = MGH(n, a, b)
print("Massiv:", natija)
