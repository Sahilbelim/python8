# write a program to 10 number ,sum ,avarege,maximum,minimum;

numbers=[]

def get_Number():
    size=int(input("Enter Size of numbers : "))
    for i in range(size):
        num=int(input(f"Enter Number {i+1} : "))
        numbers.append(num)
    

def SumOfNumber(numbers):

    sum=0
    for i in numbers:
        sum+=i
        # sum=sum+i
    return sum    


def AvgOfNumber(numbers):

    sum=SumOfNumber(numbers)
    lenth=len(numbers)
    # print(lenth)
    # print(sum)
    avg=sum/lenth
    # print(avg)
    return avg

def Max_Num(numbers):
  
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num

def Min_Num(numbers):
    min_number = numbers[0]

    for i in numbers:
        if i < min_number:
            min_number = i

    return min_number



br=200

while br!=404 :

    get_Number()

    print("Select any number for oparetion ")
    print("1 for Addition")
    print("2 for Average")
    print("3 for Maximum Number")
    print("4 for Minimum Number")



    choise=int(input(" Choise any one number  : "))




    if choise==1:

        sum=SumOfNumber(numbers)
        print(f"Sum of All Number {sum}")

    elif choise==2:

        avg=AvgOfNumber(numbers)
        print(f"avrege  of All Number {avg}")


    elif choise==3:

        max=Max_Num(numbers)
        print(f"maximum  of All Number {max}")

    elif choise==4:

        min=Min_Num(numbers)
        print(f"minimum  of All Number {min}")

   
    else:
        print("Choose valide number (invalide input ) \n")

    numbers.clear()

    choise=int(input("if you want to  continue : Enter 1 else 0 for exit "))

    if choise==0:
        br=404


    