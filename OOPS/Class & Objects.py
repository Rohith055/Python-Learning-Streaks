class comp:
    # In class we can able to mention two things one is Attributes and Behaviours
    # Attributes -> Variables
    # Behaviours -> Methods [Functions]
    def con(self):# Defining a method or a Func
        print("This program is performing on a system with the confiuration of i5 11th Gen G7")


a = '5'
print(type(a))
# Creating a Object
com1 = comp()
com2 = comp()
print(type(com1)) # It prints the class type and name.
# It calls the functions of the class
# classname.methodname(variable)
# Here we need to give the method name inside the parenthesis
comp.con(com1)
comp.con(com2)

# Here the another method is Methodname.functname()
com1.con()