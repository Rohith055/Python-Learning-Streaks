class comp:
    
    def __init__(self):
        self.name = 'R O H I'
        self.age = 20

    def update(self):
        self.age = 19

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = comp()
c2 = comp()

# Here we need to compare these two vallues using the comparing statement
# Also we need to create a separate method for the compare also in the previous steps.

if c1.compare(c2):
    print("The  have the same age category")
else:
    print("they have the Different age category")

print(c1.name)
print(c1.age)
# Size of the object depends on the number of variable.