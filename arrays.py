from array import *

vals = array('i',[5,9,6,5,-8,74,87])
# The "i" (Signed Integer)could manage the both negative and positive values.
# The "I" (Unsigned Integer)could not able to contain the negative values.

# FOR COPYING THE ARRAY OF OLD VLAUES TO NEW ARRAY
newarr = array(vals.typecode,(a for a in vals))

for e in newarr:
    print(e,",",end="")
print()

print(vals)
print(vals.buffer_info())# It simply gives the size of the array.
# 1 st is the address and the second is the size of the array.
vals.reverse()#It reverses the arr values
print(vals)
 # To print the values one by one.
for i in range(len(vals)):# Here you can give the length of array or no.of.values in the array.
    print(vals[i])
print()
# While loop in arrays

i = 0
while i<len(newarr):
    print(newarr[i],",",end="")
    i += 1

