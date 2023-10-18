
def Lenth(words):
    count=0
    for i in words:
        # print(i)
        if(i!=" "):
            count+=1

    return count



name=input("Enter Name : ")

print(f"Value of name : {name}")

sizeOfName=Lenth(name)

print(f"Numbers of Letter in name is {sizeOfName}")