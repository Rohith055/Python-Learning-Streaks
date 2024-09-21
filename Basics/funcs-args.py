
def update(r):
    r = 10
    print(id(r))
    print("x", r)

    print(id(lst))
    lst[1] = 25
    print("lsti", lst)


lst = [15,20,25,30]
print(id(lst))
update(lst)
print("lst", lst)
