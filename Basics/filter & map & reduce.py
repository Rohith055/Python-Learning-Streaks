from functools import reduce

# filter(Functions,iterables)
# In this we are going to use the filter functions associated with the lambda

def is_even(n):
    return n%2 == 0
num = [1,2,3,4,5,6,7,8,9,10,11,12]
even= (list(filter(is_even,num)))
print(even)

# Instead of this above method we're going to use this method

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
evens = (list(filter(lambda n : n%2==0,nums)))
print(evens)

# Here the filter functions are used to filter the values 
# --------------------------------------------------------
# map(function,iteables)
# Next we are going to use the map function

def update(n):
    return n*2

double = (list(map(update,evens)))
print(double)

# Instead of doing this we are going to give it as a lambda 

double1 = (list(map(lambda n : n*2,evens)))
print(double1)
# -----------------------------------------------------------
# reduce(functions,sequence)

#In the reduce func we can reduce the list of values by performing certain functional logic in to it
#Like the previous ones we are defining the reduce using the lambda func

red = reduce(lambda a,b : a*b,double1)
# To Use the reduce function we have to import it
# from functools import reduce
print(red)