import random 

dice=[1,2,3,4,5,6]

ch=0

while ch==0:

     number=random.choice(dice)

     if number==1:
          print("-------")
          print("|  *  |")
          print("|     |")
          print("-------")

     elif number==2:
          print("-------")
          print("| *   |")
          print("|   * |")
          print("-------")
     elif number==3:
          print("------")
          print("|  *  |")
          print("| * * |")
          print("-------")      

     elif number==4:
          print("------")
          print("| * * |")
          print("| * * |")
          print("-------")     

     elif number==5:
          print("------")
          print("| * * |")
          print("|  *  |")
          print("| * * |")
          print("-------")     


     else:
          print("------")
          print("| * * |")
          print("| * * |")
          print("| * * |")
          print("-------")   

     ch=int(input("Enter 0 if can continue : "))     


