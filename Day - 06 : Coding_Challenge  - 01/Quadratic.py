# Program to calculate quadratic equation (ax^2 + bx + c) roots

# Importing complex math module
import cmath

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

# Calculating the discriminant
d = (b**2) - (4*a*c)

# Calculating the solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

# Printing the roots
print('\nThe roots of {:.2f}x^2 + {:.2f}x + {:.2f} are'.format(a,b,c),'{0} and {1}.'.format(sol1,sol2))