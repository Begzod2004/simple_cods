def RO(s, s0):
    index = s.rfind(s0)  
    if index != -1:
        return s[:index]
    else:
        return s

s = input("s satrni kiriting: ")
s0 = input("s0 satrni kiriting: ")

result = RO(s, s0)
print("Natija:", result)
