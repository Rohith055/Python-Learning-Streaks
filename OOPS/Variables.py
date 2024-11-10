# Here the variables are classified as Instance Variable and Class Variable.
# Class varialbe are also Known as the static variables.
class sys:
    RAM = '8GB'# The variable created here are known to be class variable.
    def __init__ (self):
        # The variable created here is a Instance variable. Which is created under the init function.
        self.processor = "Intel i5 11-Gen G7"
        self.brand = "ASUS VivoBook 15"
# The above we've created the instance variable.

c1= sys() 
c2 = sys()
# Here it creates for two varibles under one object.

# Updating the Variable1.
c1.brand = "HP"
# Updating the class variable.
sys.RAM = "16GB"# Here it will affect all the Instances varibles and objects

print(c1.processor,c1.brand,c1.RAM)
print(c2.processor,c2.brand,c2.RAM)