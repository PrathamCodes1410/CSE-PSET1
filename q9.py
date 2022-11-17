# Q) Write a program to find the sum of n numbers using while loop  

num = int(input("Enter the number: "))
sum = 0
i = 1
while(i < (num+1)):
    sum =  sum + i
    i = i + 1
print(sum)