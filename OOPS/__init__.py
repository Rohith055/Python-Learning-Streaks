# Here we are going to see about the __init__

# For that like provious program Class and Oject 

class computer():


# Here the __init__ is been used to initialize the functions or methods automatically
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("the config is:",self.cpu,self.ram)
# Pass the obj parameter to the method
con1 = computer('i5','8gb ram')
con2 = computer('amd 5','8gb ram')
# Call the obj func 
con1.config()
con2.config()