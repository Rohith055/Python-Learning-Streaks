#
# a=0
# b=1
#
# count = 2
# n = (int(input("Enter the number:")))
# while count <= n:
#     temp = a
#     a = b
#     b += temp
#     count +=1
#
# print(f"The {n} th fibonacci number is:{b}")

def fibo(n):
    r = 0
    s = 1
    if n == 1:
        print(r)
    else:
        print(r)
        print(s)
        for i in range(2,n):
            t = r + s
            r = s
            s = t
            print(t)
fibo(10)