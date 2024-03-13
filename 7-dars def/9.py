def IPS(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k /= 5
    return k == 1

def CP(numbers):
    count = 0
    for num in numbers:
        if IPS(num):
            count += 1
    return count

numbers = [1, 5, 25, 7, 125, 30, 1250, 11, 625, 20]
result = CP(numbers)
print("Sonlar miqdori -", result)
