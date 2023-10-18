# write a program to findout factorial of given number 
# number = 5 
# factorial 5 x 4 x 3 x 2 x 1 = 120
number = int(input("enter number to get it's factorial"))
answer = 1

while number>=1:
    answer = number * answer # 5 = 5 * 1 
    number = number - 1 # 4
print(answer)