#Program to check if a number is prime

n = int(input("Enter a number : "))
if(n<2):
    print(f"{n} is not a prime number.")
else:
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            print(n,"is not a prime number.")
            break
    else:
        print(n,"is a prime number.")