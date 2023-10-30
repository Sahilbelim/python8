class student :

    

    def __init__(self):
        self.name=input("Enter Value of Name ")
        self.age=int(input("Enter Value of Age "))
        self.number=input("Enter Value of Number ")
        self.email=input("Enter Value of Email ")
        self.height=int(input("Enter Value of Height"))
        self.weight=int(input("Enter Value of Weight"))

    def printdata(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Number : {self.number}")
        print(f"Email : {self.email}")

    def data(self):
        print(f"Hello {self.Name } ,Your Age is {self.age} ")
    
    def get_bmi(self):
        bmi=self.weight/(self.height**2)
        print(f"Bmi : {bmi}")




print("Enter Value of Studet 1")
s1=student()


print("Enter Value of Studet 2")
s2=student()


s1.printdata()
s1.data()
s1.get_bmi()
s2.printdata()

s2.data()
