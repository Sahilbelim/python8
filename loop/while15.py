#write a program to findout whether given number is prime number or not 
number = int(input("Enter number to check whether it is prime number or not")) #5
divider = 2
stop = number - 1

while divider<=stop:
    reminder = number % divider #1 
    if reminder == 0:
        print("it is not prime number")
        break
    else:
        divider=divider + 1

if divider==number:
    print("it is prime number")
    
    