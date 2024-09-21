# Keyword variable length Arguments

def person(name,**data):
    print(name)
    print(data)
    # User need not to fill all the data so we are taking the corresponding values from the user
    # Here we are using the i and j to print the key-values pairs
    for i,j in data.items():
        print(i,j)

# Here you also need to mention the keyword. Because it will not accept the non keyword arguments
person('Rohi',age = 20,city = 'Sivakasi',phoneno = 1234567890)