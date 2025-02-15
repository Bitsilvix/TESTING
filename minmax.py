a = 0
by = 0
ba = 100
while a != 6:
    a=a + 1
    flo=float(input())
    if ba >= flo:
        ba=flo
    if by <= flo:
        by=flo
print(round(ba, 2))
print(round(by, 2))