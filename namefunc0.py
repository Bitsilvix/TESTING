def nametime():
    a=int(input("Input "))
    c = a
    while (a!=0):
        a=int(input("Input two "))
        if a == 0:
            return(c)
        c = c*a
print(nametime())