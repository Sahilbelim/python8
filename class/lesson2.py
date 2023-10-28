class student: # class
    number =10 #class Variable

    def __init__(self,number,name,age): #contructure
        self.no= number #Instance Variable
        self.name=name
        self.age=age
    def read(self): # method
        print("Student Read ")


s1=student(1,"sahil",18)

print(s1.no)
print(s1.name)
print(s1.age)

s2=student(2,"param",19)

print(s2.no)
print(s2.name)
print(s2.age)

s3=student(3,"hars",18)
print(s3.no)
print(s3.name)
print(s3.age)


