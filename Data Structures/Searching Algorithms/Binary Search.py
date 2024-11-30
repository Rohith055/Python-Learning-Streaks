# Here we are going to See about the binary search 
pos = -1                                # Assigning the Pos val to -1. then only it starts the count with 0
def src(list,n):
    l = 0                               # Assigning the Loweer bound value to 0
    u = len(list) - 1                   # Assigning the Upper Bound value to the length of list - 1
    while l <= u :
        mid = (l + u) //2               # Assigning the Mid Func using the Lower & Upper bounds
        if list[mid] == n:              # If target value equals to mid
            globals()['pos'] = mid
            return True
        else:                           # else the side of the search is been switched.
            if list[mid] < n :
                l = mid
            else:
                u = mid
list = [1,2,3,4,5,6,7,8,9,10]           # List of the Values
n = int(input("Enter the Element to search:"))      # Target value

if src(list,n):
    print("Element found at index of:",pos)
else:
    print("Element not found in the given list.")