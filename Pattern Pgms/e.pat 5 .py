n = (int(input("Enter the number:")))
# Printing the Square with Halfly space filled and the remaining are +

for i in range(n):
    # Ranges from 0 - n , It ranges upto n
    for j in range(i,n):
    # Ranges stops on n, It prints the Decreasing order of space.
        print(" ",end=" ")
    for j in range(i+1):
    # It prints the increasing order of +    
        print("+", end=" ")
    print()
    