
single_student={
    'name':"",
    'age':0,
    'number':"",
    'Email':""

}

data=[]
def get_UserDetail(num):
    
    for i in range(num):
        print(f"Enter Detaile of Student {i+1}")
        name=input("Enter  name : ")
        age=int(input("Enter  Age : "))
        number=input("Enter  Number : ")
        email=input("Enter  Email :")
        single_student["name"]=name
        single_student["age"]=age
        single_student["number"]=number
        single_student["Email"]=email
        data.append(single_student)


def printStudentData():

    n=0
    for i in data:
        n+=1
        print(f"Detaile of Studet {n} : ")
        print(f"Name   : {i['name']}")
        print(f"Age    :{i['age']}")
        print(f"Number :{i['number']}")
        print(f"Email  :{i['Email']}")



number_of_student=int(input("Enter Number of Student : "))

get_UserDetail(number_of_student)

printStudentData()







