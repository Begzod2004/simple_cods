def GP(b, q, n):
    if n <= 1:
        return "n o'zgaruvchisi 1 dan katta bo'lishi kerak"

    progression = [] 

    for i in range(n):
        progression.append(b * q ** i)

    return progression

b = int(input("Birinchi hadini kiriting: "))
q = int(input("Ko'paytmasini kiriting: "))
n = int(input("n ni kiriting: "))

result = GP(b, q, n)
print(f"Dastlabki {n} ta geometrik progressiya hadi: {result}")
