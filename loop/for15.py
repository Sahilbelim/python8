'''

     1
   2   2   
  3     3
4        4
5 5 5 5 5 5   


'''
k=5

for row in range(5):
    for col in range(k):
        
        print(" ",end='')


    for col in range(row+1):

        if (col==0 or row==4 or row==col):
            print(f"{row+1} ",end='')
        else:
            print(f"  ",end='')

    print("")
    k-=1