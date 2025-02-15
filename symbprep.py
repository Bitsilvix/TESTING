a="a.p.p.l.e."
b=".,;:></?[]()-=_+&*^%$#@!~`"
c=""
for symb in a:
    if symb not in b:
        c=c+symb
print(c)