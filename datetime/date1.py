from datetime import date

# datetime.date(yyyy,mm,dd)

Date=int(input("Enter Date "))
month=int(input("Enter Month  "))
year=int(input("Enter  Year  "))

FullDate= date(year,month,Date)

print(FullDate)