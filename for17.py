# 1+2+... +10 =55

#1+4+9+16+25


number=int(input("Enter Number "))
sum=0
for i in range(1,number+1):
    print(i*i)
    sum=sum+(i*i)

print("___________________________")    
print(f"{sum}")    