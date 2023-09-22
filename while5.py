# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 300.

num1=2
num2=1
print(num1," ,",end='')
print(num2," ,",end='')

while num1<123:
    num1=num1+num2  # 3
    print(num1," ,",end='')
    num2=num1+num2 #4
    print(num2," ,",end='')

# num1=num1+num2 #7
# print(num1," ,",end='')
# num2=num2+num1
# print(num2," ,",end='')

# num1=num1+num2
# print(num1," ,",end='')
# num2=num2+num1
# print(num2," ,",end='')

print("Good bye ")