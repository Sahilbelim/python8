

def Fact(num=1):
    fact=1
    
    for i in range(1,num+1,1):
        # print(i)
        fact=fact*i
    
    return fact


number=int(input("Enter Value of number "))

# print(number)

factorial =Fact(number)

print(f"Facctorial of given number {number}! : {factorial}")
factorial =Fact()
print(f"Facctorial of given number ! : {factorial}")