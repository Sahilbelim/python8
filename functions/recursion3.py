
def Add(number):
    if(number>0):

        additon =number+Add(number-1)

        return additon
    
    else:
        return 0
    

addtion= Add(5)  

print(f"Addition of Given number {addtion}")

