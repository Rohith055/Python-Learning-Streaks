

# Creating a Functions


def greets():# def function name
    print("HElLO")
    print("Welcome to Python")

#Calling the functions , If you should not call the functions it doesn't works


def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d

greets()
result1,result2 = add_sub(5,4)
print(result1)
print(result2)