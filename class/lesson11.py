class student: # class
    
    pi=3.14159 #class Variable

    def __init__(self,number,name,age,email): #contructure
        self.no= number #Instance Variable
        self.name=name
        self.age=age
        self.__email=email
        
    def emailP(self): # method
        print(f"Student Email {self.__email} ")


s1=student(1,"sahil",18,"sahil@gmail.com")


print(s1.no)
print(s1.name)
print(s1.age)
s1.emailP()
s1.email="harsh@gmail.com"
print(s1.email)
s1.__email="param@gmail.com"
print(s1.__email)



