# Here we are going to see about the Linear Search in Python.

# Here we are going to use the methods to find the value of a linked is found or not found

# For printing the position of the element we have to implement the global variable.

pos = -1                              # Here we are assigning the -1 because then only the indexing starts from the 0

def src(list,n):
    i = 0
    while i<len(list):                # If i is lesser than the length of the list proceed the following operations.
        if list[i] == n:
            globals()['pos'] = i      # If we are declaring the 'pos' here means it wiil be considered as a global variable which does not assigns the '-1' so we are using the global 
            return True
        i += 1
    return False

list = [1,2,3,4,5,6,7]                # Set of List Values.
n = (int(input("Enter the Number:"))) # Getting the input from the user.

if src (list,n):                      # Method Name 
    print("Element found at the index of", pos)
else:
    print("element Not Found")