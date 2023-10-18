numbers=[]

def number(n):
    for i in range(n):
        num=int(input(f"Enter Number {i+1} : "))
        numbers.append(num)

def SumOfNumber(numbers):

    sum=0
    for i in numbers:
        sum+=i
        # sum=sum+i
        
    lenth=len(numbers)    
    avg=sum/lenth    
    
    return sum,avg   
number(5)
result=SumOfNumber(numbers)

print(result)