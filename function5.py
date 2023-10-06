

def Lenth(Words):
    count=0
    for i in Words:
        count+=1
    # print(i)
    return count
 

name=input("Enter Your Name : ")

print(f"Name : {name}")

# number =Lenth("Sahil")
number=Lenth(name)

print(f"{number} Letters in Your Name ")
