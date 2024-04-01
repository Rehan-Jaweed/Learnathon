#Function for grading

def grade_converter(marks):
    match marks:
        case m if m >= 90:
            return "A"
        case m if m >= 80:
            return "B"
        case m if m >= 70:
            return "C"
        case m if m >= 50:
            return "D"
        case _:
            return "F"

marks = int(input("Enter your marks : "))
grade = grade_converter(marks)
print("Final Grade :",grade)