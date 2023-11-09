
class BMI:

    def get_bmi(self,height,weight):
        bmi=weight/(height**2)

        return bmi
    
class meter_height(BMI):
    def __init__(self):
        self.foot_height=int(input("Enter your height in foot"))
        self.inch_height=int(input("Enter your height in inch"))
        self.weight=float(input("Enter your weight in kg "))

    def foot_meters(self):
    
        meters=self.foot_height/3.281
        # print(meters)
        return meters    
     
    def inch_meters(self):
    
        meters=self.inch_height/39.37
        # print(meters)
        return meters     
    
    def full_height(self):
        
        height=self.inch_meters()+self.foot_meters()
        
        return   height
    def printAllData(self):
        bmi=self.get_bmi(weight=self.weight, height=self.full_height())
    
        print(f"BMI : {bmi}")
        print(f"Height : {self.full_height()}")
        print(f"Weight : {self.weight}")
p1=meter_height()

# bmi=p1.get_bmi(height=1.5239256324291375,weight=48.36)

# height=p1.full_height()

# print(height)

# bmi=p1.get_bmi(height=p1.full_height(), weight=p1.weight)
# print(bmi)
p1.printAllData()
