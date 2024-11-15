# Here we are going to perform about the decorators
def div(x,y):
    return x/y
res=div(2,4)
print(res)
# In the above program we need to swap the values for obtaining the int value as 2.0 (Float)
# For that we have to use conditional statements for swapping the values
# In some scenario the file is not accessible or changalable. In that case we have to use the decorators

def div1(a,b):
    print(a/b)

def decor_div(func):# In here we have to give a function to be performed
    # decor_div is a decorator that takes another function as an argument in this case, div1
    def inner_decor(a,b):# In here we have to pass the variables of the div1
        # This inner function is responsible for modifying the behavior of the original div1
        if a < b:
            a,b = b,a
# (to avoid dividing by a smaller number, which might not be desirable in some cases, like integer division).
        return func(a,b)# We are returning the a,b to the main func
    return inner_decor# we are returning the inner also 
div1 = decor_div(div1)# In here we have to pass the func as div
div1(2,4)
    # Simply the decorators are been used for changing the behaviour of the oringinal func