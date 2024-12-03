# Date time package in python
import datetime as dt
# find date
current_date=dt.date.today()
print("current date: ",current_date)
print((current_date.year))
print((current_date.month))
print((current_date.day))
c=dt.date(2023,5,15)
print(c)
print("----------------------------------------------")
# find time and date
current_time=dt.datetime.now()
print(current_time)
time=dt.time(3,50,20,56555)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

print("----------------------------------------------")
# Difference between time

c= dt.datetime.now()
d= dt.datetime(2011,12,15,4,50,10,00)
difference=c-d
print(difference)
print("----------------------------------------------")
# using different design formatings in output

c=dt.datetime.now()
print(c)
s=c.strftime("%A %B %d %y")
print(s)


