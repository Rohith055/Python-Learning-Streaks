n =(int(input("Enter the number:")))


# Here we are going to print the star patterns all=ternatively to form a Diamond Pattern
for i in range(n):
    # First we are printing the increasing order of the spaces
    for j in range(i,n):
        print(" ",end=" ")
    # Next we are printing the increasing order of the stars
    for j in range(i+1):
        print("+",end=" ")
    # Next we are printing the Increasing order of the stars with repsect to i
    for j in range (i):
        print("+",end=" ")
    print()
    # Similarly we are doing this with just opposite to the previous form
for k in range(n):
    # First we are printing the increasing order of the spaces
    for l in range(k+1):
        print(" ",end=" ")
    # Next we are printing the decreasing order od stars
    for l in range(k,n):
        print("+",end=" ")
    # Next we are printing the decreasing order of the stars
    for l in range(k,n-1):
        print("+",end=" ")
    print()

    '''
    Can you notice that we are giving n-1 on all alternative patterns because it prints the stars of first five in a same rows just like below
                                               + + + + + + + + + +
                                                + + + + + + + +
                                                  + + + + + +
                                                    + + + +
                                                      + +
    To avoid printing like these type of stars only we are giving the n-1 or i on range func
    
    '''