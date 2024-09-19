
a=0
b=1

count = 2
n = (int(input("Enter the number:")))
while count <= n:
    temp = a
    a = b
    b += temp
    count +=1

print(f"The {n} th fibonacci number is:{b}")