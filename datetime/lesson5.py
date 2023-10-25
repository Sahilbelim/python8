from datetime import date

Year=int(input("Enter Year : "))
Month=int(input("Enter Month  : "))
Day=int(input("Enter day  : "))


date1=date(day=Day,year=Year,month=Month)

print(f"First Date : {date1}")

Year=int(input("Enter Year : "))
Month=int(input("Enter Month  : "))
Day=int(input("Enter day  : "))

date2=date(Year,Month,Day)

print(f"Second Date : {date2}")

# difference between two dates 
final_date=date1-date2

print(f"Final Date : {final_date}")