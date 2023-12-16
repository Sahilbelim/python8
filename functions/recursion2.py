num=5
def Fact(num):
    
    if(num>1):

        fact=num*Fact(num-1)
        return fact
    
    else:
        return 1 
   

factorial=Fact(7)   

print(factorial)