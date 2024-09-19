from array import *

ar = array('i',[])
# Getting the Length of the array from the user
n = (int(input("Enter the length")))

for i in range(n):
    # Here we are getting the values of array
    x = (int(input("Enter the value:")))
    ar.append(x)
print(ar)

val = int(input("Enter a value to search:"))
k = 0
for j in ar:
    if j==val:
        print("the index of arr is:",k)
    k += 1

#There is an another method in printing the index of a array
print("Using the index method:", ar.index(val))