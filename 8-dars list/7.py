def CHTY(n):
    teskari_n = n[::-1]  
    for element in teskari_n:
        print(element, end=" ")  

n = int(input("mass uzunligini kiriting: "))
n = []

for i in range(n):
    element = int(input(f"{i+1}-elementni kiriting: "))
    n.append(element)

print("massning teskari tartibdagi ko'rinishi:")
CHTY(n)
