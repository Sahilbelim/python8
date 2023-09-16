# write a program to find bmi and also check condition .
weight=float(input("Enter your Weight : "))
foot_h=int(input("Enter your Height in Foot : "))
inch_h=int(input("Enter your Height in Inch : "))

print(f"Your Weight : {weight}")
print(f"Your Height in Foot  : {foot_h}")
print(f"Your Height in Inch  : {inch_h}")

f_to_m=foot_h/3.281
i_to_m=inch_h/39.37
# print(f"Foot to meter {f_to_m}")
# print(f"Inch to meter {i_to_m}")
height=f_to_m+i_to_m

BMI=weight/(height*height)

print(f"|||||||||||||||||||||||||| BMI  = {BMI}  ||||||||||||||||||||||||||")

# check condition of bmi 

if (BMI>0 and BMI<18):
    print("||||||||||||||||||||||||||You are UnderWeight|||||||||||||||||||||||||| ")
elif (BMI>18 and BMI<25):
    print("||||||||||||||||||||||||||You are Normal ||||||||||||||||||||||||||")
elif (BMI>25 and BMI<30):    
    print("||||||||||||||||||||||||||You are OverWeight ||||||||||||||||||||||||||")
elif (BMI>30 and BMI<35):
    print("||||||||||||||||||||||||||You are Obese ||||||||||||||||||||||||||")
elif(BMI>=35):
    print("||||||||||||||||||||||||||You are ExtremObese||||||||||||||||||||||||||")
else:
    print("||||||||||||||||||||||||||Invalide Input ||||||||||||||||||||||||||")    