from numpy import *
"""
arr = array([1,2,3,4,5])
# It adds 5 to all elements in the array
arr = arr +5
print(arr)
"""

# Adding the two arrays.
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,0])
arr3 = arr1 + arr2
print(arr3)

# Finding the math operations in array.
arr4 = array([1,2,3,4,5])
print(sin(arr4))# It gives the sin value of each and every element in an array.
# similarly for cos and tan and log values and square root also
print(sin(arr4))
print(tan(arr4))
print(log(arr4))
print(sqrt(arr4))
print(sum(arr4))# Sum of the array
print(min(arr4))# Min of the array
print(max(arr4))# Max of the array

# Sorting a array
arr5 = array([4,73,43,453,433,564])
print(sort(arr5))

# Concatenate a array
arr6 = array([1,2,3,4,5])
arr7 = array([4,73,43,453,433,564])
print(concatenate([arr6,arr7]))

