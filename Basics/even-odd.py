

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+= 1
        else:
            odd+= 1

    return even,odd
lst = [25,26,27,28,29,30,31,32,33,34,35,36]

even, odd = count(lst)

print("even : {} and odd : {}".format(even, odd))