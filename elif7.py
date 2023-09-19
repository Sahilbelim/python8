number1=int(input("Enter Value of number 1 "))
number2=int(input("Enter Value of number 2 "))
number3=int(input("Enter Value of number 3 "))

# print(f"Number 1 is {number1}")
# print(f"Number 2 is {number2}")
# print(f"Number 3 is {number3}")

if(number1>number2 and number1>number3):
    print(f"Number 1 is Greater and Value of number 1 {number1}")
elif(number2>number1 and number2>number3):    
    print(f"Number 2 is Greater and Value of number 2 {number2}")
elif(number3>number1 and number3>number2):    
    print(f"Number 3 is Greater and Value of number 3 {number3}")
elif(number1==number2 and number1>number3): 
    print(f"Number 1 and 2 are Greater and Value of number  {number1}")
elif(number2==number3 and number2>number1): 
    print(f"Number 2 and 3 are Greater and Value of number  {number2}")
elif(number3==number1 and number3>number2): 
    print(f"Number 1 and 3 are Greater and Value of number  {number3}")
else:    
    print(f"All are same  and Value of numbers  {number3}")