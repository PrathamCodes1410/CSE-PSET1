# Q) Write a program to print all the numbers between 1000 and 2000 
#    which are divisible by 7 but are not a multiple of 5.

i = 1000
for i in range(2000):
    if((i % 7) == 0) and ((i % 5) != 0) and (i > 1000):
        print(i)