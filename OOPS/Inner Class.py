

class student: # Outer Class

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
# Here the objects for the outer class will be declared anywhere on the inner class 
# which it will  executes before the outer class objects got executed. 
        self.laptop = self.lap()
    
    def show(self):
        print(self.name , self.rollno)
        self.laptop.show() # It will executes the Inner class 

    # Here we are going to declare the inner class

    class lap: # Inner class
        def __init__(self):
            self.brand = 'ASUS'
            self.model = 'Vivobook'
            self.processor = 'i5 11th Gen'
            self.ram = '8gb'
            # With the common class we can able to create one or more different objects 
        def show(self):
            print(self.brand,self.model,self.processor,self.ram)

s1 = student('R O H I',953722104043)
s1.show()

# we can call it on outside the class also.
# lap1 = s1.lap()
# lap1.show()