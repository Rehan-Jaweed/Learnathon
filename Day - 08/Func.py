#Function to add two numbers

def sum_numbers(num1, num2):
    return num1 + num2

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
result = sum_numbers(a,b)
print(f"Sum : {result}")