def fms(s):
    index1 = s.find('1')  
    index2 = s.find('2')  
    
    if index1 != -1 and index2 != -1:
        return s[index1+1:index2]
    else:
        return s.strip()

satr = input("Satrni kiriting: ")
natija = fms(satr)
print("Natija:", natija)
