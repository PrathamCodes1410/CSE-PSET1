# Q) Write a Python program to count the number of even and odd numbers from a series of numbers

num  = int(input("Enter the no. of numbers: "))
even = 0
odd = 0

for i in range(num):
    no = int(input("Enter your number: "))

    if((no % 2) == 0):
        even =  even + 1
    else:
        odd = odd + 1

print(f"The number even numbers are: {even}")
print(f"The number of odd numbers are: {odd}")