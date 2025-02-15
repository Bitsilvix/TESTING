import random
col = 0
c=[]
for i in range(100):
    a = random.random()
    c.append(round(a, 2))
c.sort()
def abc():
    k=0
    while k != 100:
        print(c[k:k+10])
        k=k+10
abc()