# Program to find largest of three numbers

x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))
z = float(input("Enter the third number : "))

if(x >= y) and (x >= z):
    largest = x
elif(y >= x) and (y >= z):
    largest = y
else:
    largest = z

print("The largest number from {:.2f}, {:.2f} and {:.2f} is {:.2f}.".format(x,y,z,largest))