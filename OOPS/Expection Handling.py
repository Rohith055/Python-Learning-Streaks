# Here we are going to see about the errors, and they are classified into three types they are 
# Logical Error -> Error Occurs in Logic
# Runtime Error -> Error Occurs in Runtime
# Syntax Error -> Error Occurs in Syntax

# Nextly we are going to see about the Exception Handling

a = 5
b = 0

# Here we are going to try to divide these two numbers a&b
# Else we are going to display the Statement Divide by 0 is not possible

try:
    print(a/b)
except Exception:
    print("You can't Divide the number with 0. Hence It Displays DivideByZero Error")

print("Ends")

