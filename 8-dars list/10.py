def J_V_T_I(massiv):
    J_I = [i for i, x in enumerate(massiv) if x % 2 == 0] 
    T_I = [i for i, x in enumerate(massiv) if x % 2 != 0]  
    return J_I, T_I

n = int(input("Massiv uzunligini kiriting: "))
massiv = []

for i in range(n):
    element = int(input(f"{i+1}-elementni kiriting: "))
    massiv.append(element)

J_I, T_I = J_V_T_I(massiv)

J_I.sort()
T_I.sort(reverse=True)


print("Massiv:")
for i in J_I:
    print(f"{i}-indeks: {massiv[i]} (juft)")
for i in T_I:
    print(f"{i}-indeks: {massiv[i]} (toq)")
