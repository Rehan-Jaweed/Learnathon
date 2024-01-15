# String functions

# Taking input
string = input("Enter the first string : ")
string2 = input("Enter the second string : ")

# isstring Functions
print("Is the first string uppercase? --",string.isupper())
print("Is the second string lowercase? --",string2.islower())
print("Does the first string contain alphanumeric characters? --",string.isalnum())
print("Does the first string contain whitespaces? --",string.isspace())
print("Does the second string contain digits? --",string2.isdigit())
print("Does the second string contain alphabets? --",string2.isalpha())

# General Functions
print("First string :",string.swapcase(),"and second string :",string2.swapcase(),"after swapping their cases.")
print("Number of charecters in the first string :",len(string))
print("Number of charecters in the second string :",len(string2))
string3 = input("Enter the string you want to check in first string : ")
print("Number of times",string3,"appears in first string :",string.count(string3))
