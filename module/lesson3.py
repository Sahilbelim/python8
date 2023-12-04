import datetime

temp=dir(datetime)
print(temp)
pi=3.14

def getpi():
    
    global pi
    pi=3.14159628
    # print(pi)
getpi()
print(pi)