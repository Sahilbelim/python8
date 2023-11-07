
# 1/1 + ,1/2 , ... , 1/n

j=0
k=1
sum=0
number=int(input("Enter Value of number "))
while(j<number):

    j+=1
    k=1/j
    sum+=k
    print(f"1/{j} ",end='')


print(f"\nSum Of Given patter : {sum}")


# j+=1
# k=1/j
# print(f"1/{j} ",end='')

# j+=1
# k=1/j
# print(f"1/{j} ",end='')