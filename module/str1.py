


# name=input("Enter Name : ")
# print(f"\n Name : {name.upper()}")
# print(f"\n Name : {name.lower()}")


temp="10"

print(str.isalnum(temp))
print(str.isalpha(temp))
print(str.isnumeric(temp))

temp="Sahil"

print(str.istitle(temp))

temp="SAHIL"
print(str.islower(temp))
temp="sahil"
print(str.isupper(temp))

temp=input("Enter name ")
if str.isspace(temp):
    
    print(f"Valide input : {temp}")

else:
    print("Invalide input don't use space in name ")