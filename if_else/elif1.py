number1=int(input("Enter Number 1 "))
number2=int(input("Enter Number 2 "))

# print(f"Value of number 1 {number1}")
# print(f"Value of number 2 {number2}")

# print(number1>number2)

if number1>number2:
    print("Numeber 1 is bigger then number 2 ")
    print(f"Value of number 1 is {number1}")

elif number2>number1:
    print("Numeber2 is bigger then number 1 ")
    print(f"Value of number 2 is {number2}")
elif number1==number2:
    print("Number 1 and Number 2 are Same ")
    print(f"Value of number 1 {number1} and Value of number 2 {number2}")
else:
    print("Invalide input ")            
