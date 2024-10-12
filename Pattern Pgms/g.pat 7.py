n = (int(input("Enter the number:")))
'''
Here we are going to print the inverted hill form of triangle

'''
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i):     
        print("+",end=" ") 
    for j in range(i+1):
        print("+",end=" ")
  
    print()






