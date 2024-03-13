def T_S_O_M(massiv):
    toq_sonlar_o_sish = [x for x in massiv if x % 2 != 0]  
    return toq_sonlar_o_sish

def T_S_S_M(massiv):
    toq_sonlar_o_sish = T_S_O_M(massiv)
    return len(toq_sonlar_o_sish)

n = int(input("Massiv uzunligini kiriting: "))
massiv = []


for i in range(n):
    element = int(input(f"{i+1}-elementni kiriting: "))
    massiv.append(element)

toq_sonlar_o_sish = T_S_O_M(massiv)
sorted_toq_sonlar_o_sish = sorted(toq_sonlar_o_sish, reverse=True)

print("Berilgan massivdagi barcha toq sonlarni o'z ichiga oladigan elementlar tartibida:")
for element in sorted_toq_sonlar_o_sish:
    print(element)

T_S_S_M = T_S_S_M(massiv)
print("Barcha toq sonlar miqdori:", T_S_S_M)
