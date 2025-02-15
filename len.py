a = str(input("ten symb: ")) 
if len(a) > 10:
    print ("Iz kastryuli sbel kotletu cho za bretto bretto bretto CHO ZA BRETTO")
elif len(a) <= 10:
    b = 10 - len(a)
    print(a+"*"*b)