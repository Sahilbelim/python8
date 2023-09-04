name=["sahil","harsh","param","darshan23","vasu34","pratham"]
list1=["45.36","25","belim","85","patel"]
name2=['sahezad ','shahid']
print(name)
print(list1)

print(name[0])
print(name[1] *5)
print(name[2])
print(name[3])
print(name[4])

print("Weight : ",list1[0])

print(list1[1:3])


print(list1[2:])

print(list1+name)

name.append("dishant bhai") # add new iteam 

print(name)

name.append("yagnesh bhai ")

print(name)

name.extend(name2) #add new list

print(name)

name.insert(3,"deep")

print(name)

list1.remove("belim")

print(list1)

student_name = name2.pop(1)

print(name2)

print(student_name)

name.append(student_name)

print(name)

num=name.index("harsh")

print("index of aliment ",num)

Count =name.count("dishant bhai")

print("number of name how many time ",Count)

name.sort()

print(name)

list1.sort()
print(list1)

name.reverse()
print(name)

print("name 3 print below")

name3=name.copy()

name3.sort()

print(name3)
print("line no 73  ")

name.clear()

print(name)
