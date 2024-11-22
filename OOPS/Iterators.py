


# num = [0,1,2,3,4,5,6,7,8,9,10]
# # print(num(0)) A method for printing the Num according to the Index values
# # for i in num:
# #     print(i)
#     # These are the normal methods of printing the numbers using the index values but here we are going to see about the topic called Iterators.

# # A function that will pass the list into iterators. "iter"

# lst = iter(num)
# # print(lst.__next__())# It will print the first value of the converted iterator.
# # print(lst.__next__())# Then it will produce the next value
# # The __next__ will also removes the duplicate values also.
# for i in num:
#     print(lst.__next__())


# Here we are going to print the top ten numbers using the Iterators
class Ten:
    
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
    
        # To avoid printing the excess number we are using the conditonal stmts
    
        if self.num <= 10:
            vald = self.num # Here we should return the self.num so only we are assigning this to a separate variable.
            self.num += 1
            return vald
    
        else: # To stop the loop we are raising the exception using the "raise" Statement.
            raise StopIteration #To Stop the "None" Values printing in the output terminal.

v1 = Ten()

for i in v1:    # After running this code we are unalbe to stop the printing of None to avoid the issue we are using the else.
    print(i) # here we need to print "i" instead for printing the __next__ Because we've already defined the __next__ in the method separately.