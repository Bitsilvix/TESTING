from random import randint
max=100
for i in range(10):
    a = randint(-100,100)
    print(a)
    if a < max:
        max = a
print(max)