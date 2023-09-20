# Check if a character is a vowel or a consonant.

letter=input("Enter letter ")

print(f"Letter : {letter}")

if(letter in 'aeiouAEIOU'):
    print("It's Vovel")
else:    
    print("It's consonant")