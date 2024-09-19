for i in range(5):
    if i == 3:
        continue# it stops the current execution only
    elif i == 4:
        pass # it asumes it as empty and passes the current loop

    elif i ==5:
        break # It breaks the entire loop

else:
    print("there is no element present in it")
    i += 1
