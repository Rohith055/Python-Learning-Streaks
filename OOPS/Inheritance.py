# Here we are going to see about the inheritance 

# Inheritance is nothing but a new class can have the access to the values to the previous class.
class A():
    def demo1(self):
        print("demo 1 is working")
    def demo2(self):
        print("demo 2 is working")

# a1 = A()

# a1.demo1()
# a1.demo2()

# Here the above class is working which is been called as single inheritance 

class B(A):
    
    def demo3(self):
        print("demo 3 is working")
        
    def demo4(self):
        print("demo 4 is working")
class C(B):
    
    def demo6(self):
        print("demo 5 is working")
        
    def demo5(self):
        print("demo 6 is working")


b1 = B()

b1.demo3()
b1.demo4()

c1 = C()

c1.demo5()
c1.demo6()

# Here we can able to access the all other classes from the newly created class

# The above is known as the multi level Inheritance.