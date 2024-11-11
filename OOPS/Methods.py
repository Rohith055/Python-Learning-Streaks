'''
Here we are going to see about the methods 
Here the methods are classified into three types
Which is 
> Instance Method
> Class Method
> Static Method 

Here we've already seen that in variables in that the class and the static variable are same 
But in the methods it will be often classified into different categories.
'''

class student:
    school = 'ROHI ENGG & TECH'
    def __init__(self,s1,s2,s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
    def avg(self):
        return(self.s1 + self.s2 + self.s3) / 3 
    def get_s1(self):
        return s1 # Setter only sets the values
    def set_s1(self,value):
        return s1 # Setters only sets the values
    
    @classmethod # Here we need to mention the class method to use the class method
    def s_info(cls):
        return cls.school
    
    @staticmethod # Here we need to mention the class method to use the static method
    def info():
        print(" The Department of these students is CSE.")


m1 = student(75,80,90)
m2 = student(65,75,80)

print(m1.avg())
print(m2.avg())

print(student.s_info()) # Print statement of the class method.
student.info()

# In Instance Methods there are two types in it 
# they are 
# Accessors -> used to fetch values only.
# Mutators -> Used to Modify the values.
