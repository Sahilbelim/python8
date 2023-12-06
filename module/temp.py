X=[]
Y=[]
XY=[]
X2=[]
Y2=[]

Num=int(input("Enter the size of x and y : "))

for i in range(Num):
    x=float(input(f"Enter the X{i+1} : "))
    X.append(x)

for i in range(Num):
    y=float(input(f"Enter the Y{i+1} : "))
    Y.append(y)

for i in range(Num):
    xy=X[i]*Y[i]
    XY.append(xy)

for i in range(Num):
    x2=X[i]*X[i]
    X2.append(x2)

for i in range(Num):
    y2=Y[i]*Y[i]
    Y2.append(y2)

sum1=0
for i in range(Num):
    sum1+=X[i]

sum2=0
for i in range(Num):
    sum2+=Y[i]

sum3=0
for i in range(Num):
    sum3+=XY[i]

sum4=0
for i in range(Num):
    sum4+=X2[i]

sum5=0
for i in range(Num):
    sum5+=Y2[i]

print("")
print(f"X = {X}")
print(f"Y = {Y}")
print(f"XY = {XY}")
print(f"X2 = {X2}")
print(f"Y2 = {Y2}")
print("")
print(f"SUM of X = {sum1}")
print(f"SUM of Y = {sum2}")
print(f"SUM of XY = {sum3}")
print(f"SUM of X2 = {sum4}")
print(f"SUM of Y2 = {sum5}")


ans =Num*((sum3) -((sum1)*sum2))/((Num*((sum4)-(sum1*sum1)))*(Num(sum5)-(sum2*sum2)))