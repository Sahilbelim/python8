
class scylinder:
    pi=3.1415962
    def __init__(self):
        self.height=int(input("Enter Value of Height "))
        self.radius=int(input("Enter Value of Radius "))
     
    def getArea(self):  
        area=(2*self.pi*self.height*self.radius)+(2*self.pi*(self.radius**2))
        return area
    # def getValume(self):

    def printArea(self):
        print(self.getArea())

    def printData(self):
        print(f"Height : {self.height}\nradius : {self.radius}")


        
print("First Scylinder")
s1=scylinder()
print("Second Scylinder")
s2=scylinder()

s1.printData()

s1.printArea()

s2.printData()

s2.printArea()