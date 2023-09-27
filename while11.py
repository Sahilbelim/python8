temp=5
row=1

while row<=5:
    col=1
    while col<=temp:
        if(row==1 or col==1 or temp==col):
            print(f"* ",end='')
        else:    
            print("  ",end='')
        col+=1
    print("")
    row+=1
    temp-=1
