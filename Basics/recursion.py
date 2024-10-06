# Using recursion
# Calling a function from itself

import sys

# To set the recursion limit
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())# By default it has 1000

i = 0 # Here the value of i is global to all funcs
def greet():

    global i # Here the i is global so we're calling it as a global variable.
    i += 1
    print("hello World",i)
    greet()  #Calling the function repeatedly intself which has a limit upto 1000

greet()