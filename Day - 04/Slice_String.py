# Program that prints the string between 4 and 10 index

# Input
string = input("Enter a sentence : ")

# Checks if the sentence has 10 characters
if len(string) >= 10:
    string2 = string[4:10]
    print("Extracted Substring :", string2)
else:
    print("Your string doesn't have 10 characters.")
