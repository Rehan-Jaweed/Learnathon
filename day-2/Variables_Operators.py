# Variables and Data Types
int_ = int(input("Enter an integer : "))
float_ = float(input("Enter a floating point number : "))
bool_ = True
str_ = input("Enter a string : ")

print("\nVariables and Data Types:")
print("Integer :", int_)
print("Float :", float_)
print("Boolean :", bool_)
print("String :", str_)

# Operators
a = int(input("\n\nEnter the first integer : "))
b = int(input("Enter the second integer : "))

# Arithmetic Operators
print("\nArithmetic Operators :")
print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division : {:.2f}".format(a / b))
print("Modulus :", a % b)
print("Exponentiation :", a ** b)
print("Floor Division :", a // b)

# Comparison Operators
print("\nComparison Operators :")
print("a is equal b? --", a == b)
print("a is not equal to b? --", a != b)
print("a is greater than b? --", a > b)
print("a is greater than or equal to b? --", a >= b)
print("a is less than b? --", a < b)
print("a is less than or equal to b? --", a <= b)