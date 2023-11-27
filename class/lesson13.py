class student: # class
    
    __email=input("Emter Value of Email ") #class Variable
    
    def emailP(self): # method
        print(f"Student Email {self.__email} ")

s1=student()
# print(s1.__email)  Error 
s1.emailP()
print(s1._student__email)
