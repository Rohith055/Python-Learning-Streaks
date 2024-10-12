n = (int(input("Enter the number:")))
'''

> Printing the Square with Halfly space filled and the remaining are +
> Here we're going to print the hill form 
> For that we;re first printing the decreasing the spaces
> Then the increasing triangle 
> then we are printing the another increasing triangle

'''
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("+",end=" ")
    for j in range (i+1):
        print("+",end=" ")
    print()