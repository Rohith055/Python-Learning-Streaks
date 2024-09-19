from numpy import *

arr1 =array([
        [1,2,3,7,8,9],
        [4,5,6,10,11,12]
    ])
# (flatten()) is used to combine both the rows and the colums as a single one dimensional arr
arr2 = arr1.flatten()
# reshape is for creating a multiple arrays with the given values
# arr3 = arr2.reshape(3,4)

arr3 = arr2.reshape(2,2,3)
# Here it creates two (2-Dimensional array) with 3 values in it.

print(arr2)
print(arr3)

# It gives the num.of.rows and num.of.cols
print(arr1.shape)
# It gives the size of the array.
print(arr1.size)