def IPN(k, n):
    if k <= 0 or n <= 1:
        return False
    while k % n == 0:
        k //= n
    return k == 1

def CPO(numbers, n):
    count = 0
    for num in numbers:
        if IPN(num, n):
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 2  
result = CPO(numbers, n)
print(f"{n} ning darajalariga teng bo'lgan sonlar miqdori:", result)
