def AP(a, d, n):
    if n <= 1:
        return "n o'zgaruvchisi 1 dan katta bo'lishi kerak"
    
    progression = []  

    for i in range(n):
        progression.append(a + i * d)

    return progression


a = 2
d = 3
n = 5
result = AP(a, d, n)
print(f"Dastlabki {n} ta arifmetik progressiya hadi: {result}")
