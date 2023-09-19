#  Determine the largest of three numbers using nested if-else.
number1=int(input("Enter Value of number 1 "))
number2=int(input("Enter Value of number 2 "))
number3=int(input("Enter Value of number 3 "))

# print(f"Number 1 is {number1}")
# print(f"Number 2 is {number2}")
# print(f"Number 3 is {number3}")

if(number1>number2):
    if(number1>number3):

        print(f"Number 1 is large Value of number 1 {number1}")

    elif(number3>number1):
        
        print(f"Number 3 is large Value of number 3 {number3}")

    else:    

        print(f"Both are same Value of number 1 and 3 is {number1}")

elif(number2>number1):
    if(number2>number3):

        print(f"Number 2 is large Value of number 2 {number2}")

    elif(number3>number2):

        print(f"Number 3 is large Value of number 3 {number3}")

    else:

        print(f"Both are same Value of number 2 and 3 is {number2}")
        
else:
    if (number1==number2==number3 ):

        print(f"All are same Value of number 1 , 2 and 3 are  {number1}")

    else:

        print(f"Both are same Value of number 1 and 2 is {number1}")
         
