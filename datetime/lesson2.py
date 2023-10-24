import datetime

year=int(input("Enter Year : "))
month=int(input("Enter Month  : "))
day=int(input("Enter day  : "))

dob=datetime.datetime(year,month,day)
print(dob)
dobTs=dob.timestamp()
print(dobTs)

date_dob=datetime.date.fromtimestamp(dobTs)

print(date_dob)





