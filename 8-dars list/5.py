def GN(n):
    n = [1, 1] 
    for i in range(2, n):
        n.append(n[i-2] + n[i-1])  
    return n

def ISH(n):
    if n <= 2:
        return "n must be greater than 2"
    n_series = GN(n)
    return n_series[:n]

n = int(input("Enter the value of n (n > 2): "))
b = ISH(n)
print(n, b)
