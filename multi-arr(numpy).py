from numpy import *

# arr = array([1,2,3,4,5],'i')
# print(arr)

# Multiple ways in creating the numpy.

# arr1 = array([1,2,3,4,5.0])
# print(arr1.dtype)#Knowing the data type of an array
# print(arr1)# If either one of the values in the array is float means all the others becomes float.

# Using linspace() Function which is present only in numpy.
# It includes the start, stop, step and it quite similar to the range function
# In range the stop is exculded but here it includes the stop value also.
# Here the step is meant for splitting the values in to num.of.parts.
# By default it splits into 50 parts.
## arr2 = linspace(0,15,16)# Here the given is splitted into 16 parts
## print(arr2)


# The another way of printing an array using arange.
# It does not print the stop values prints all values before the stop value.
# arr3 = arange(1,15,2)
# print(arr3)

# Next we are using the logspace
# arr4 = [logspace(1,40,5)]
# print('%.2f', arr4[0])


# Using Zeros method we're creating the array.
arr5 = zeros(5,int)
print(arr5)

# Using ones method we're creating the array.
arr6 = ones(5,int)
print(arr6)
