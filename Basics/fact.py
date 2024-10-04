"""
Creating the Factorial values
With the help of function and the logic
"""

def fact(n):

    r = 1
    for i in range(1,n+1):
        r = r * i
        print(r)
    return r
# With using the function method
x = 5
result = fact(x)
# print(result)