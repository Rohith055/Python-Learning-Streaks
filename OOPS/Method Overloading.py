# Here we are going to See about the the method overloading and overiding

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None):
        if a!=None and b!=None and c!=None:
            r = a + b + c
        elif a!=None and b!=None:
            r = a + b
        else:
            r = a
        return r
    
s1 = student(98,87)
# print(s1.sum()) # Here it shows the error of positional arguments missing which is the values are necessary for the operation is to be performed.

# the alternative way is to fix the values as none. Which shows no error and by default it fixes the none as the default value.

print(s1.sum(1,2,3)) # with this output it will shows the correct output.