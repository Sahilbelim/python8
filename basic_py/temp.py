import sys

numbers=[]

def number(n):
    for i in range(n):
        num=int(input(f"Enter Number {i+1} : "))
        numbers.append(num)
        
def add(number):
    sum=0
    for i in number:
        sum+=i
    return sum
  
def avg(number):
    Addition=add(number)
    lenth=len(number)
    avg=Addition/lenth
    return avg

def Max_Num(number):
  
    max_num = number[0]
    for i in number:
        if i > max_num:
            max_num = i
    return max_num
    

def Min_Num(number):
    min_number = number[0]

    for i in number:
        if i < min_number:
            min_number = i

    return min_number

while True:
    print("Menu")
    print("1.Addition")
    print("2.Average")
    print("3.Maximum Number")
    print("4.Minimum Number")
    print("5.Exit")
    print("")

    choise=int(input("Enter Choise : "))
    print("")
    
    if (choise==1):
        nums=int(input("Enter numbers you want : "))
        number(nums)
        print("")
        Addition=add(numbers)
        print(f"Addition of all numbers is {Addition}")
        print("")
    elif (choise==2):
        nums=int(input("Enter numbers you want : "))
        number(nums)
        print("")
        Average=avg(numbers)
        print(f"Average of all number is {Average}")
        print("")
    elif (choise==3):
        nums=int(input("Enter numbers you want : "))
        number(nums)
        print("")
        Max=Max_Num(numbers)
        print(f"Maximum Number is {Max}")
        print("")
    elif (choise==4):
        nums=int(input("Enter numbers you want : "))
        number(nums)
        print("")
        Min=Min_Num(numbers)
        print(f"Minimum Number is {Min}")
        print("")
    elif (choise==5):
        sys.exit(0)
    else:
        print("Invalid Choise")

