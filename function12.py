# write a program to 10 number ,sum ,avarege,maximum,minimum;

numbers=[]

def AddNumber(lenth):

    for i in range(lenth):

        number=int(input(f"Enter Value of number {i+1} :"))

        numbers.append(number)

def SumOfNumber(numbers):

    sum=0
    for i in numbers:
        sum+=i
        # sum=sum+i
    return sum    


def AvgOfNumber(numbers):

    sum=SumOfNumber(numbers)
    lenth=len(numbers)
    avg=sum/lenth

    return avg

AddNumber(3)

sum =SumOfNumber(numbers)

print(f"Sum Of All Element :{sum}")

avg=AvgOfNumber(numbers)

print(avg)
print(numbers)
