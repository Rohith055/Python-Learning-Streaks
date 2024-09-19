num = (int(input("enter a number")))
for i in range(2,num):
    if num % i ==0: # It is a very basic way in finding the prime number.
        print("Not a Prime number")
        break
else:
    print("prime Number")