# Copying an array

from numpy import *

# It is a basic method for copying an array.
arr1 = array([1,2,3,4,5])
arr2 = arr1
print(arr2)
print(arr1)
# Knowing the id of an arr
print(id(arr2))
print(id(arr1))

# Another method of copying an array.
# First we are going to see about the shallow copy

arr3 = array([5,6,7,8,9,10])
# By using this we are copying an array
arr4 = arr3.view()
# The view function will gives a shallow copy of an array
# Next we are changing the value of a arr3 only
arr3[1] = 11
# Lets print this whther the value changes on a single array(arr3) or the both the arrys (arr4)
print(arr4)
print(arr3)
# In result it changes the values of both the arrays



arr5 = array([5,6,7,8,9,10])
# By using this we are copying an array
arr6 = arr5.copy()
# The view function will gives a Deep copy of an array
# Next we are changing the value of a arr5 only
arr5[1] = 11
# Lets print this whether the value changes on a single array(arr5) or the both the arrys (arr6)
print(arr5)
print(arr6)
# In result it changes the values of a single array(arr3) the arrays