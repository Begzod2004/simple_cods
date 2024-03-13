import datetime

day = int(input("Tug'ilgan kuningizni kiriting:"))
month = int(input("Tug'ilgan oyingizni kiriting:"))
year = int(input("Tug'ilgan yilingizni kiriting:"))

birth = datetime.datetime(year,month,day)
now  = datetime.datetime.now()

difference = now - birth

b = difference.days < 10000
print(difference)
print("b = ",b)