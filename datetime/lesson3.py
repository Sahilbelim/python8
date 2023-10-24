import datetime

# datenow=datetime.datetime.now()
# print(datenow)
my_hour=int(input("Enter Value of Hour : "))
my_min=int(input("Enter Value of min : "))
my_sec=int(input("Enter Value of sec : "))


my_time=datetime.time(my_hour,my_min,my_sec)
print(f"full Time : {my_time}")
print(f"Hour : {my_time.hour}")
print(f"minute : {my_time.minute}")
print(f"seconds : {my_time.second}")
print(f"microsecond : {my_time.microsecond}")