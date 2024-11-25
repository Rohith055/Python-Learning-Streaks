# Here we are going to see about the errors, and they are classified into three types they are 
# Logical Error -> Error Occurs in Logic
# Runtime Error -> Error Occurs in Runtime
# Syntax Error -> Error Occurs in Syntax
# Nextly we are going to see about the Exception Handling

a = 5
b = 5

# Here we are going to try to divide these two numbers a&b
# Else we are going to display the Statement Divide by 0 is not possible

try:
    print("Resource Open")
    print(a/b)
    # print("Resource Close") Here the exception will be runs so the "Resource Ends " will not works
    # Lets try something to get as a input 
    r = int(input("Enter the Number:"))
    print(r)# Here in the Input Suppose we are giving a String instead of Integer. It shows the ValueError.

# Here the Exception can able to handle multiple values.

except ZeroDivisionError as z:
    print("The Divide by Zero Operation is not possible", z)

except ValueError as v:
    print("The Value Does not supports the given Datatype, You are supposed to give a Integer.",v)
    
except Exception as e:
    print("Something Went Wrong...", e)
    # print("Resource Ends")
# Here to print the enstatement or any other function "Finally" is used 

finally:
    print("Resource Ends") # It will be executed separatly even the Exception is not executed.
