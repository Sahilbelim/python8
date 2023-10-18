import datetime


currentDateTime=datetime.datetime.now()

print(f"Current Date & Time : {currentDateTime}")

TodayDate=datetime.date.today()


print(f"Date : {TodayDate}")

date=TodayDate.day
month=TodayDate.month
year=TodayDate.year


print(f"Today Date Only : {date}")
print(f"Today month Only : {month}")
print(f"Today year Only : {year}")