
k=5

for row in range(5):
    # print(row)
    for col1 in range(row+1):
        print(" ",end='')

    for col2 in range(k):

        if (col2==0 or row==0 or (col2+1)==k):
            print(f"* ",end='')
        else:
            print("  ",end='')
    print("")
    k-=1
  
# for col1 in range(5):
#     print("_",end='')

# for col2 in range(5):
#     print("*",end='')
# print("")

# for col1 in range(5):
#     print("_",end='')

# for col2 in range(5):
#     print("*",end='')

# print("") 

# for col1 in range(5):
#     print("_",end='')

# for col2 in range(5):
#     print("*",end='')

# print("")    

# for col1 in range(5):
#     print("_",end='')

# for col2 in range(5):
#     print("*",end='')

# print("")    
