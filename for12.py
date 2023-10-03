


for row in range(5):
    # print(row)
    for col1 in range(row+1):
        print(" ",end='')

    for col2 in range(5-row):

        if (col2==0 or row==0 or col2==(4-row)):
            print(f"* ",end='')
        else:
            print("  ",end='')
    print("")
  
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
