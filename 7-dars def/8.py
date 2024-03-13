def ish():
    son = son[::-1]
    a = 0
    for i in range(len(son)):
        a += 2 ** i * int(son[i])
    print(a)



son = input('ikkilik son kiriting: ')