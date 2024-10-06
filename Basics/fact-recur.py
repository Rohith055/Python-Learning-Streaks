
# Here we are getting the input from the user and giving it to the funcs fact
x = (int(input("Enter the number to find the facrtorial:")))

def fact(x):
    # If the x is 0 means it needs to print the value  1
    if(x == 0):
        return 1
    """
    
    We're Performing the fact in recursion like this
    
    5 * fact(5-1) = 5 * 4!
    4 * fact(4-1) = 4 * 3!
    3 * fact(3-1) = 3 * 2!
    2 * fact(2-1) = 2 * 1!
    1 * fact(1-1) = 1 * 0!
    """
    return x * (fact(x-1))
result = fact(x)# Calling the defined func fact
print(result)