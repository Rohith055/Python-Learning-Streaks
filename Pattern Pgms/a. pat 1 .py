nums = (int(input("Enter the number :")))
# Getting the input from the user 
for i in range (1,nums+1):
    # the range starts from 1 and it increements the num+1 
    # eg: num = 5
    # i = (1,2,3,4,5)
    for j in range(1,i+1):
        # Here the j will have the range from 1 to i+1
        print("*",end="")
    print()