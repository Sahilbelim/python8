# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15 

k=1
row=1

while row<=5:
    col=1
    while col<=row:
        print(f"{k} ",end='')
        k+=1
        col+=1
    print("")
    row+=1
