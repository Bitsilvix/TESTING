s="Купите пожалуйста новый маркер"
lst=[]
i=0
while True:
    i=s.find(" ")
    lst.append(s[ :i])
    a=s[i+1: ]
    print(a)
    print(i)
    print(lst)
print(lst)