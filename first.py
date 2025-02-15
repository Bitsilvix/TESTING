a=str(input("Знак:"))
b,c = int(input("Первое число: ")), int(input("Второе число: "))
if a =='+':
    print(b+c) 
elif a =='-':
    print(b-c) 
elif a =='*':
    print(b*c) 
elif a =='/':
    if c==0:
        print ("Syntax error")
    else:
        print(b/c)
elif a =="//":
    if c==0:
        print ("Syntax error")
    else:
        print(b//c) 
elif a =='%':
    if c==0:
        print ("Syntax error")
    else:
        print(b%c) 