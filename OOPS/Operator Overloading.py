
# a = '5'
# b = '6'
# print(a + b)
# print(int.__add__(a,b))
# Both are printing the same result.
# print(str.__add__(a,b))
# Here we need to add the strings means we need to use the str.__add__(a,b)

# All the operators behind the screen workd as a methods. They initially calls the values and add those values and produce the output.

class student:

    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2

    def __add__(self,other): # we can try various methods which are overloads as they are used as raw. we can use it alternatively using the methods.
        s1 = self.s1 + other.s1
        s2 = self.s2 + other.s2
        s3 = student(s1,s2)
        return s3
    
    def __gt__(self,other):

        r1 = self.s1 + self.s2
        r2 = other.s1 + other.s2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.s1 , self.s2) # Here the curly brackets will be replaced by the values. here it will prints the values without any brackets only the value is being printed.
    # After Including this method it will prints the correct values only instead of the address.
           
s1 = student(99,89)
s2 = student(98,87)

# s3 = s1 + s2 Here the compiler doesn't know how to add the student and a student. In which both the holds the int values.
# So we're supposed to define the add method separately.

s3 = s1 + s2 # -> student.__add__(s1,s2)
print(s3.s1)

if s1 > s2:
    print("S1 Wins the Battle")
else:
    print("S2 Wins the Battle")
 
a = 5
print(a.__str__()) # It will prints the value
print(s1.__str__())# It will prints the adress. Behind the screen it will executes the inbuilt func __str__
# Here the both of the methods are calling the func __Str__ in the behind the process
# Here we need to override this methods to print its actual values instead of address.