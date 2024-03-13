from funtools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def son(a: int) -> bool:
    if a % 2 == 0:
        return True
    else:
        return False

a = list(map(son, a))
print(a)



