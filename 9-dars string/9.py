def RS(s, s1, s2):
    index = s.find(s1)  
    if index != -1:
        return s[:index] + s2 + s[index+len(s1):]
    else:
        return s

s = input("s satrni kiriting: ")
s1 = input("s1 satrni kiriting: ")
s2 = input("s2 satrni kiriting: ")

result = RS(s, s1, s2)
print("Natija:", result)
