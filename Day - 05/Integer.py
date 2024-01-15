# Program to check whether the number is positive or negative

num = float(input("Enter an integer : "))
if(num > 0):
    print(num,"is a positive number.")
elif(num == 0):
    print(num,"is neither positive nor negative. It is zero.")
else:
    print(num,"is a negative number.")