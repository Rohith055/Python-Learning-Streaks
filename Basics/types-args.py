
def person(name,age):

    print(name)
    print(age)

# We are passing the arguments in the function
person(age = 20, name = 'rohith')


# Fixing the default values in funcs
# If we are finxing a values in the func we need not to call it at last
def person1(name,age=19):
    print(name)
    print(age)

# We are passing the arguments in the function
# No need to call the age because it is fixed as a default value
person1(name = 'rohith')



# *b Means ot contains the multiple values
def sum(a,*b):
    # c = a + b # Here the b is a tuple we can't add a int to a tuple
    print(a)
    print(b)
    # So we are adding the each values to b with the help of looping concepts
    c = 0
    for i in b: # It adds the every element in the b and store it in c
        c += i
    print(c)

# Here the b assings the remaining values(6,7,8,9) as a tuple
sum(5,6,7,8,9)





