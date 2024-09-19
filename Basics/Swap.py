a = 5
b = 55
# Basic normal method for swapping the number
#temp = a
#a = b
#b = temp
# Second method for swapping the values using the formula method
#a = a - b
#b = a - b
#a = a + b
# The another method for swapping the two values using X-OR
#Because the x-or reduces the usage of bits
a = a ^ b
b = a ^ b
a = a ^ b


# These are the three methods for swapping a value
print(a)
print(b)