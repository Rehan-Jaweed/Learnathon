# Program to grade student's marks

marks = float(input('Enter marks of the child out of 100 : '))
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
else:
    print("F")