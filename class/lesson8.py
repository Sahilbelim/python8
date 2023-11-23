class teacher:

    def __init__(self):
        self.no=int(input("Enter Value of teacher no. : "))
        self.name =input("Enter Value of teacher Name : ")
        self.Class=input("Enter Value of teacher class. : ")
        self.age=int(input("Enter Value of teacher age"))

    def printData(self):
        print(f"No.: {self.no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.Class}")

    def teach(self):
        print("Teacher can teach ")


class Student:

    def __init__(self):
        self.rollNo=int(input("Enter Value of Roll Number of Student "))
        self.name=input("Enter Value of Student Name " )
        self.age=int(input("Enter Value of Student Age"))
        self.std=int(input("Enter Value of Student STD : "))

    def printStdData(self):

        print(f"Student {self.rollNo}")
        print(f"Student Name: {self.name}")    
        print(f"Student Name: {self.age}")    
        print(f"Student Name: {self.std}")

    def read(self):
        print("Student can read ")

    def write(self):
        print("Student can write ")

class principal(teacher,Student):

    def __init__(self):
        self.name=input("Enter Name of Principal " )
        self.email=input("Enter Email of Principal " )
        self.number=input("Enter Number of Principal " )
        teacher.__init__(self)
        Student.__init__(self)

    def printP(self):
        print(f"principal Name :  {self.name}")    
        print(f"principal Eamil :  {self.email}")    
        print(f"principal Number :  {self.number}")    

    def manage(self):   
        print("Principal can manage ")


p1=principal()

# student Methods
print("||||||||||||||||||||| student Methods |||||||||||||||||||||||||")
p1.printStdData()
p1.read()
p1.write()

# teacher  Methods

print("||||||||||||||||||||| teacher Methods |||||||||||||||||||||||||")
p1.printData()
p1.teach()

# principal  Methods

print("||||||||||||||||||||| principal Methods |||||||||||||||||||||||||")
p1.printP()
p1.manage()

