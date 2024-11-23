# # The Generators will have the Iterators

# def sample():

#     yield 5 # Here the Yield is the generator which generates the Iterators
# # Here the yield is also similar to the Return Func 
# val = sample()
# print(val)


def Sqrt():
    n=1
    while n<=10:
        srt = n*n
        yield srt # It generates the iterators 
        n += 1


vd = Sqrt()
for i in vd:
    print(i)
