n = (int(input("Enter the number:")))

# Printing the Decreasing order right angled triangle pattern

for i in range(n):
    # Ranges upto n
    for j in range(i,n):
    # Ranges upto i - n    
        print("+",end=" ")
    print()
    