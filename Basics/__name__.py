from calcop2 import sub

# Here we are going to see about the special variable name 

def res():
    sub()# Here the sub prints the __name__ which contains the module name 
    # It prevents the collision of function calling.
    # it is morely used in performing the module actions.
    print("Res is ")
def res2():
    print("Res 2 is ")
def res3():
    print("Res is ",__name__)

def main():
    res()
    res2()
    res3()
main()
