# Q) Write a program to calculate factorial of a number using for loop

fac = int(input("Enter a number: "))
num = 1
for i in range(fac):
    num = num * (i+1)

print(num)