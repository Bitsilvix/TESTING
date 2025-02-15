def getInput():
    a = input()
    try:
        b=int(a)
    except:
        ValueError()
    return b
a=input()
def testInput(a):
    
    a=int()
    try:
        c=int(a)
        prt="True"
    except ValueError():
        prt="False"
    return (c, prt)
def strToint(a):
    try:
        a=int()
        return a
    except ValueError:
        print("False")
        return
def printint(a):
    print("chozabretta")
    return
print(getInput())

print(testInput(a))

print(strToint(a))
print(printint(a))