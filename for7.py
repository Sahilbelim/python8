start_num=int(input("Enter Starting number "))
End_num=int(input("Enter Ending number "))
temp=int(input("Enter Increament or decreament "))
for num in range(start_num,(End_num+1),temp):
    print(f" {num} ,",end='')