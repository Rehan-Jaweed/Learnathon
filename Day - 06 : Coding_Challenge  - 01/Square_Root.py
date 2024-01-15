# Program to calculate square root

# Importing math module
from math import sqrt as s

num = float(input("Enter your number : "))
sqrt = s(num)

print("The square root of {:.3f} is {:.3f}.".format(num,sqrt))