n = (int(input("Enter the number:")))
'''
Here we are going to print the inverted hill form of triangle

'''
for i in range(n):
    for j in range(i):
        # Increasing Order of the Space 
        print(" ",end=" ")
    for j in range(i,n):     
        # Decreasing Order of the Stars
        print("+",end=" ") 
    for j in range(i,n-1):
        # Decreasing Order of the Stars in repect to n-1 to achive the hill like structure.
        print("+",end=" ")
  
    print()