# write a program to findout simple interest of given amount, rate & year 
amount = int(input("Enter amunt"))
rate = int(input("Enter rate"))
year = int(input("Enter year"))

interest = (amount * rate * year) / 100
print(interest)