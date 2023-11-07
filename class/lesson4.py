
class bmi :

    def __init__ (self):
        self.name=input("Enter Value of Name ")
        self.foot=int(input("Enter Value of Height in Foot "))
        self.inch=int(input("Enter Value of Height in Inch "))
        self.weight=float((input("Enter Value of Weigth in kg ")))

    def meter_foot(self):
        meter =self.foot/3.281

        # print(meter)
        return meter
    
    def meter_inch(self):
        meter =self.inch/39.37

        # print(meter)
        return meter
    
    def meter_height(self):

        height= self.meter_foot()+self.meter_inch()
        # print(height)
        return height

    def get_bmi(self):
        height=(self.meter_height())
        bmi=self.weight/(height**2)
        print(f"Name : {self.name}")
        print(f"Bmi : {bmi}")    


p1=bmi()

# p1.meter_foot()
# p1.meter_inch()
# p1.meter_height()
p1.get_bmi()