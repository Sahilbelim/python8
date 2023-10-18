# write a program to check given year is miliniymyear or not.
year = int(input("Enter year "))

print(f"Given Year is {year}")
m_year=year%1000
# print(m_year)
if m_year==0:
    print("Given Year is miliniymyear")
else:
    print("Given Year is not  miliniymyear")

print("good bye ")    