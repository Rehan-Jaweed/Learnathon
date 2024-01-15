# Program to calculate price of ticket

age = int(input("Enter your age : "))
time = int(input("Enter the time of show to closest hour in 24-hour format : "))

match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
        price = 0
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
        price = 5
    case 13 | 14 | 15 | 16 | 17 | 18:
        price = 10
    case _:
        price = 20

if time < 12:
    price -= 5

print(f"Your ticket price is ${price}")