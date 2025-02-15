a="0101"
b="1001"
def shifr(a,b):
    s=""
    for i in range(len(a)):
        if a[i]==b[i]:
            s+="0"
        else:
            s+="1"
    return s
print(shifr(a,b))
c="1100"
def shifro(c,b):
    d=""
    for i in range(len(a)):
        if c[i]==b[i]:
            d+="0"
        else:
            d+="1"
    return d
print(shifro(c,b))