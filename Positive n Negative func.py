def positive():
    print ("this number is positive")
def negative():
    print ("this number is negative")
def test():
    n=int(input("num"))
    if n > 0:
        positive()
    if n < 0:
        negative()
test()