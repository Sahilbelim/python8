# 2005 to 2023
# nom. => 1970 to 2023
# 2005 => 1970 to 2005

from datetime import datetime

timenow=datetime.now().timestamp()
year=int(input("Enter Year : "))
month=int(input("Enter Month : "))
day=int(input("Enter day : "))

givenDate=datetime(year,month,day).timestamp()
print(givenDate)
dobtimestamp=timenow-givenDate

print(f"DOB Timestamp : {dobtimestamp}")

print(f"DOB minits: {dobtimestamp/60}")
print(f"DOB House: {dobtimestamp/3600}")
print(f"DOB Day: {dobtimestamp/(3600*24)}")
print(f"DOB month: {dobtimestamp/(3600*24*30)}")
print(f"DOB Year : {dobtimestamp/(3600*24*365)}")
