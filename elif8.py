lenth1=int(input("Enter First  lenth  of triagle "))
lenth2=int(input("Enter Second  lenth  of triagle "))
lenth3=int(input("Enter Third  lenth  of triagle "))

print(f"Fist lenth : {lenth1}")
print(f"Second lenth : {lenth2}")
print(f"Third lenth : {lenth3} ")

if(lenth1==lenth2==lenth3):
    print("That Triagle is Equilateral  ")
elif(lenth1==lenth2 or lenth2==lenth3 or lenth3==lenth1):
    print("That Triagle is Isosceles  ")
else:
    print("That Triagle is Scalene   ")

print("Good bye ")    

        