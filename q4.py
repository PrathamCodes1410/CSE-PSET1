"""
 Q) Write a program that prints the numbers from 1 to 100. 
    But for multiples of three print “godly” instead of the number and for the 
    multiples of five print “badly”. For numbers which are multiples of 
    both three and five print “GodlyBadly”.
"""

for i in range(101):

    if((i % 3) == 0):
        if((i % 5) == 0):
            print("GodlyBadly")
        else:
            print("Godly")
    elif((i % 5) == 0):
        print("Badly")
    else:
        print(i)