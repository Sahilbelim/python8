name=str(input("Enter Your name : "))
weight=float(input("Enter Weight :"))
h_feet=int(input("Enter Height in feet : "))
h_inch=int(input("Enter Height in inch : "))

print("-------------------- Name : ",name," ----------------------------")
print("Weight :",weight)
print("Height in Feet :",h_feet)
print("Height in Inch :",h_inch)

feet_to_meter=h_feet/3.281
# print(feet_to_meter)
inch_to_meter = h_inch/39.37
# print(inch_to_meter)
height=feet_to_meter+inch_to_meter

BMI=weight/(height*height)

print("------------------------Your BMI = ",BMI," ----------------------------")

