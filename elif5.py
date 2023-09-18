# Write a program to display zodiac symbol & given zodiac sign from given birth day and month as per following criteria.
# https://i.pinimg.com/564x/43/aa/50/43aa50c918f3bd03abb71b6d4aaf93c7.jpg

month=int(input("Enter Month : "))
date =int(input("Enter Date : "))

print(f"Value of Month {month}")
print(f"Value of Date {date}")

if ((month==3 )and (date>=21 and date<=31) ):
    print("Zodiac sign is Aries symbol : the Ram ")
elif((month==4) and (date>=1 and date<=19)):
    print("Zodiac sign is Aries symbol : the Ram ")
elif((month==4) and (date>=20 and date<=30)):
    print("Zodiac sign is Taurus symbol : the Bull ")
elif(month==5 and(date>=1 and date<=20)):
    print("Zodiac sign is Taurus symbol : the Bull ")
elif(month==5 and (date>=21 and date<=31)):
    print("Zodiac sign is Gemini symbol : the Twins ")
elif(month==6 and (date>=1 and date<=20)):    
    print("Zodiac sign is Gemini symbol : the Twins ")
elif(month==6 and (date>=21 and date<=30)):
    print("Zodiac sign is Cencer symbol : the crab ")
elif(month==7 and (date>=1 and date<=22)):    
    print("Zodiac sign is Cencer symbol : the crab ")
elif(month==7 and (date>=23 and date<=31)):
    print("Zodiac sign is Leo symbol : the Lion ")
elif(month==8 and (date>=1 and date<=22)):
    print("Zodiac sign is Leo symbol : the Lion ")
elif(month==8 and (date>=23 and date<=31)):
    print("Zodiac sign is virgo symbol : the virgin ")
elif(month==9 and (date>=1 and date<=22)):    
    print("Zodiac sign is virgo symbol : the virgin ")
elif(month==9 and (date>=23 and date<=30)):    
    print("Zodiac sign is Libra symbol : the scales ")
elif(month==10 and (date>=1 and date<=22)):
     print("Zodiac sign is Libra symbol : the scales ")
elif(month==10 and (date>=23 and date<=31)):
     print("Zodiac sign is scandpio symbol : the scandpion ")
elif(month==11 and (date>=1 and date<=21)):
     print("Zodiac sign is scandpio symbol : the scandpion ")
elif(month==11 and (date>=22 and date<=30)):
     print("Zodiac sign is stegittarius symbol : the Archer ")
elif(month==12 and (date>=1 and date<=21)):
     print("Zodiac sign is stegittarius symbol : the Archer ")
elif(month==12 and (date>=22 and date<=31)):
     print("Zodiac sign is capricandn symbol : the goat ")
elif(month==1 and (date>=1 and date<=19)):
     print("Zodiac sign is capricandn symbol : the goat ")
elif(month==1 and (date>=20 and date<=31)):
     print("Zodiac sign is Aquarius symbol : the Water bearer ")
elif(month==2 and (date>=1 and date<=18)):
     print("Zodiac sign is Aquarius symbol : the water bearer ")
elif(month==2 and (date>=19 and date<=29)):
     print("Zodiac sign is pisces symbol : the fisher ")
elif(month==3 and (date>=1 and date<=20)):
     print("Zodiac sign is pisces symbol : the fisher ")
else:
    print("invalide input")
print("Good bye ")    