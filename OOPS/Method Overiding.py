# here in method overiding we are going to use inheritance to avoid overloading

class r:

    def show(self):
        print("In A Class")

class s(r):
    # Here pass means there is nothing inside this just proceed to the next step.
    pass #here the pass method passes the class with no attributes
# Initially it shows the no attributes defined error for avoiding that we are using the Inheritance.

a1 = s() # Here we are using the class s.
a1.show()
