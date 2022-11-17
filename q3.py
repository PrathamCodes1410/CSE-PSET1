# Write a program to check if input number is a prime number.

new = int(input("What is your number: "))

for i in range(new-2):
    if((new % (i+2)) == 0):
        print("Not a prime number")
        quit()


print("Prime Number")