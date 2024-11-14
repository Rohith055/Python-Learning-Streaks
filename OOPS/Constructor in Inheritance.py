'''
Here we are going to see about Constructors in Inheritance
A Sub class can access super class but a super class cannot have the access to sub class.
'''

class A:

    def __init__(self):
        print("__init__ in class A")

    def fea1(self):
        print("The Feature 1 is working ")
    
    def fea2(self):
        print("The Feature 2 is working ")  
    
class B(A):

    def __init__(self):
        super().__init__()
        print("__init__ in class B")

    def fea3(self):
        print("The Feature 3 is working ")
    
    def fea4(self):
        print("The Feature 4 is working ")  

class C(B):
    def __init__(self):
        super().__init__()
        print(" __init__ in C")
# In here it uses the method resolution order. It prefers to be left to right only.


# a1 = A() # Here it is a constructor which carrying the super class A
# Here the A will have the init 

# similarly for B
# a2 = B() # If the init method in class B is not present means it will go for class A which is a super class 
# If you creates for a object in B then it will first searches for the init method in B and then it searches in the class A


# a1.fea1()
# a1.fea2()

b1 = C()
b1.fea1()