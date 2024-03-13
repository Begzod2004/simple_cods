import datetime
# a = int(input("Mashinangizning nomerini kiriting:"))
# x = datetime.datetime.now().day
# if (a%2==0 and x%2==0) or (a%2!=0 and x%2!=0):
#   print("Bugun harakatlana olasiz")
# else:
#   print("Mumkin emas")



today = int(input("Kunni kirirting: "))
month = int(input("Oyni kirirting: "))
year = int(input("Yilni kirirting: "))
car_name = int(input("Mashinangizning nomerini kiriting:"))
d = datetime.datetime.now().day
m = datetime.datetime.now().month
y = datetime.datetime.now().year
if 0<today<32 and 0<month<13 and d<=today and y<=year and m<=month:
  if (car_name%2==0 and d%2==0) or (car_name%2!=0 and d%2!=0):
    print("Bugun harakatlana olasiz")
  else:
    print("Mumkin emas")
else:
  print("Sanani noto'g'ri kiritdingiz")

