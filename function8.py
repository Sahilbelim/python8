
def Squre(a,b=0):
    squre= (a*a)+(2*a*b)+(b*b)

    return squre

x=int(input("Enter Value of x "))
y=int(input("Enter Value of y "))

print(f"Value of x :{x}")
print(f"Value of y :{y}")

sq=Squre(x,y)

print(f"Squre  of x+y {sq}")

sq=Squre(x)

print(f"Squre  of x {sq}")

sq=Squre(y)

print(f"Squre  of y {sq}")