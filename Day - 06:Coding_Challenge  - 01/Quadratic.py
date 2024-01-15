# Program to calculate quadratic equation (ax^2 + bx + c) roots

# Importing complex math module
import cmath

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('\nThe solution are {0} and {1}'.format(sol1,sol2))