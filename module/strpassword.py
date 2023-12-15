import random
import string

letter=string.ascii_lowercase+string.ascii_uppercase+string.digits

size=int(input("Enter Size of Password "))

password=[]
for i in range(size):
    
    password.append(letter[random.randint(0,size)])
s=""
# print(password)

print(s.join(password))    