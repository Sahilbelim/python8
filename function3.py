# write a program to find area of cylinder 

def getPi():
    return 3.141592

pi=getPi()
radius=float(input("Enter Value of Radius "))
height=float(input("Enter Value of Height "))

print(f"Value of Radius {radius}")
print(f"Value of Height {height}")

area=(2*pi*radius*height)+(2*pi*(radius*radius))

print(f"Area of Cylinder : {area}")
