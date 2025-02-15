def namefunc():
    a=int(input("Input "))
    c = a
    col = 1
    while True:
        a=int(input("Input two "))
        if a == 0:
            return(c, col)
        if c > a:
            c = a
        col+=1
print(namefunc())