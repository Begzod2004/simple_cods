def create_odd_array(n):
    if n <= 0:
        return "n o'zgaruvchisi musbat va 0 dan katta bo'lishi kerak"
    
    odd_numbers = []  
    current_number = 1  

    while len(odd_numbers) < n:
        odd_numbers.append(current_number)
        current_number += 2  

    return odd_numbers

n = int(input("n ni kiriting: "))
result = create_odd_array(n)
print(f"{n} o'lchamli massiv: {result}")
