class teacher:
    def __init__(self):
        self.name=input("Enter teacher's Name ")
        self.age=int(input("Enter teacher's Age "))
      
    def teach(self):
        print("Teacher can teach")

    def printdata(self,name,age):
        print(f"Name : {name}")
        print(f"Age : {age}")   
        


class Student(teacher):
    
    def __init__(self):
        self.name=input("Enter student's Name ")
        self.age=int(input("Enter student's Age "))
        self.number=input("Enter teacher's Number ")
    def  write(self):
        print("Student can write")

    def read(self):
        print("Student can read")



t1=teacher()

t1.printdata(t1.name,t1.age)
t1.teach()

s1=Student()
s1.read()
s1.write()
s1.printdata(s1.name,s1.age)
s1.teach()


