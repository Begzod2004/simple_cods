def J_S_T(massiv):
    juft_sonlar = [x for x in massiv if x % 2 == 0]  
    return juft_sonlar

def J_S_M(massiv):
    juft_sonlar = J_S_T(massiv)
    return len(juft_sonlar)


n = int(input("Massiv uzunligini kiriting: "))
massiv = []

for i in range(n):
    element = int(input(f"{i+1}-elementni kiriting: "))
    massiv.append(element)

sorted_massiv = sorted(enumerate(massiv), key=lambda x: x[1])

print("Indekslari bo'yicha tartiblangan massiv:")
for index, value in sorted_massiv:
    print(f"{index}: {value}")

juft_sonlar = J_S_T(massiv)
juft_sonlar_miqdori = J_S_M(massiv)

print("Juft sonlar:", juft_sonlar)
print("Juft sonlar miqdori:", juft_sonlar_miqdori)
