#Program to add even numbers from 1 to 50

i=1
sum=0
while(i<51):
    if(i%2==0):
        sum+=i
    i+=1
print("Sum of even numbers between 1 to 50 =",sum)