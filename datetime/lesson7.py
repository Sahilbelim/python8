import datetime

DateNow=datetime.datetime.now()
print(f"Current DAte : {DateNow}")

form1=DateNow.strftime("%M:%H:%S")
print(form1)

form2=DateNow.strftime("%d/%m/%Y")

print(form2)

form3=DateNow.strftime("%d/%m/%Y  , %M:%H:%S")

print(form3)