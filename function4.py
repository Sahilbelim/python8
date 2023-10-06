
def Sub(i,j):
    return (i-j)

def Add(n1,n2):
    add=n1+n2
    return add



number1=int(input("Enter Value of Number 1 "))
number2=int(input("Enter Value of Number 2 "))

# print(f"Value of number 1 {number1}")
# print(f"Value of number 2 {number2}")

addition=Add(number1,number2)

print(f"Addition of number 1 and number 2 :  {addition}")

# temp=Sub(20,10)
temp=Sub(number2,number1)

print(f"Value of Subtraction {temp}")
