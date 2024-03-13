def RO(s, s0):
    index = s.find(s0)  
    if index != -1:
        return s[:index] + s[index+len(s0):]
    else:
        return s

s = input("s satrni kiriting: ")
s0 = input("s0 satrni kiriting: ")

result = RO(s, s0)
print("Natija:", result)
