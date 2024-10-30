def add():
    print("ADD is :")
def sub():
    print("SUB is :",__name__)

def main():
    add()
    sub()
# here the main func calls the functions in calcop2 also inorder to avoid that we are using a special variable __name__

# the __name__ variable stores the module name by default we need to change the variable name by assigning a new name
if __name__ == "__main__":
    main()

# Here if the name contains the value main it will executes the code other wise the defined functions will works as a module.