# def function1(x,y):
#   return x + y

# def function2(x,y):
#   return x - y

# def function2(x,y):
#   return x * y

# def function2(x,y):
#   return x / y

# print(function1(8,4))
# print(function1(8,4))
# print(function1(8,4))
# print(function1(8,4))



def sign(x):
  if x>0:
    return 1
  elif x==0:
    return 0
  else:
    return -1
  
x = int(input("x = "))
print(sign(x))