import datetime
import time
DateNow=datetime.datetime.now()
print(f"Current DAte : {DateNow}")

form1=DateNow.strftime("%M:%H:%S - %f")
print(form1)

form1=DateNow.strftime("%d/%m/%Y")

print(form1)

form1=DateNow.strftime("%d/%m/%Y  , %M:%H:%S")

print(form1)

form1=DateNow.strftime("%d , %a %m ")

print(form1)


form1=DateNow.strftime("%d ,  %A %m ")

print(form1)
form1=DateNow.strftime("%d , %w ")
print(form1)
form1=DateNow.strftime("%dth %b ")
print(form1)
form1=DateNow.strftime("%dth %B ")
print(form1)
form1=DateNow.strftime("%dth %B year : %y")
print(form1)
form1=DateNow.strftime(" %I:%M  ")
print(form1)
form1=DateNow.strftime(" %I:%M  %p ")
print(form1)
form1=DateNow.strftime(" day/365 : %j ")
print(form1)
form1=DateNow.strftime(" Week in year  : %U ")
print(form1)
form1=DateNow.strftime(" Week in year  : %W ")
print(form1)
form1=DateNow.strftime(" Date  : %c ")
print(form1)
form1=DateNow.strftime(" Date  : %x ")
print(form1)
form1=DateNow.strftime(" Time  : %% %X ")
print(form1)


  
formatted_date = time.strptime(" 02 Dec 1996 ",  " %d %b %Y") 
print(formatted_date) 
