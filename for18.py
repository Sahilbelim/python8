# 5!=5x4x3x2x1 =120 factorial



number=int(input("Enter Number "))
mul=1
for i in range(1,number+1):
    # print(mul)
    mul=mul*i
   
print(f"{number}!={mul}")