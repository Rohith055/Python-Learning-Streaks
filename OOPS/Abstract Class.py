# Here we are going to discudd about the ABC Abstract Base Classes (Abstract class)
    # here by default the python does n't supports the Abstract Classes.
# For Using the abstract classes we are going to use some packages called abc

from abc import ABC, abstractmethod

class dupli(ABC):
    @abstractmethod
    def nothing(self): # here the abstract class will have one abstract method.
        pass # Here the pass statement means it which there is nothing inside the method just pass it or proceed for the next step.

# For overcoming this we need to create the another class

class null(dupli):# This class inherits with the main class 'dupli'
    # pass If we are passing this class it shows error which we have to define the class. Which is done as follows
    def nothing(self):# Here the abstract classes method should be implemented 'nothing'
        print("It Works")

# d1 = dupli()# For abstract class we can't create the objects 
# d1.nothing()
# here we are going to create the object for the class which is inherited from the super class.
d2 = null()
d2.nothing()

# Derived class inheriting from Dupli
class Vend(dupli):
    def nothing(self):
        print("Vend class is working")

# Another class with a method accepting an instance of Dupli
class Venue:
    def ven(self, dupli):
        print("Venue works")
        dupli.nothing()  # Calls the 'nothing' method from the Dupli class

# Object creation and method invocation
d4 = Vend()  # Instance of Vend, which is derived from Dupli
d3 = Venue() # Instance of Venue
d3.ven(d4)   # Pass d4 (Vend object) to the ven method.

# In here it shprtly expresses the Abstract class should be inherited from all it sub classes.
# It should be the method which is called inside the abstract class is abstract method.