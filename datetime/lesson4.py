import datetime 

my_year=int(input("Enter Year : "))
my_month=int(input("Enter Month  : "))
my_day=int(input("Enter day  : "))
my_hour=int(input("Enter Value of Hour : "))
my_min=int(input("Enter Value of minut : "))
my_sec=int(input("Enter Value of second : "))
my_micro=int(input("Enter Value of microsecond : "))

full_dateTime=datetime.datetime(my_year,my_month,my_day,my_hour,my_min,my_sec,my_micro)

print(full_dateTime)
