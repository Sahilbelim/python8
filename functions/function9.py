# write program to get 5 stundet name,age and class and then print  using function 

studentData=[]

    # function can get input from user  
def get_studentData(student_number):

    for i in range(student_number):
        print(f"Enter Details of Student {i+1}")
        Name=input("Enter Your Name : ")
        Age=int(input("Enter Value of Age : "))
        Class=int(input("Enter Value of class : "))
        # data append in list 
        studentData.append(Name)
        studentData.append(Age)
        studentData.append(Class)

# display/ print list student Details 
def printStudentData(stundet):
    lenth=len(stundet)
    n=1
    for i in range(0,lenth,3):
        print(f"Detail of Student {n} ")
        print(f" Name : {stundet[i]}")
        print(f" Age : {stundet[i+1]}")
        print(f" class : {stundet[i+2]}")
        n+=1

number=int(input("Enter Number of Student "))

get_studentData(number)

printStudentData(studentData)

