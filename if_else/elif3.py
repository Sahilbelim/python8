month=int(input("Enter number of Month "))

print(f"Value of Month is {month}")

if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("Day of month is 31 ")
elif (month==2):
    print("Day of month is 28/29 ")
elif (month==4 or month==6 or month==9 or month==11):    
    print("Day of month is 30 ")
else:
    print("Invalide month ")    