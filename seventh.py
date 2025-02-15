s = str(input())
l=len(s)//2
for i in range(l):
    if s[i]!=s[-1]:
        print("ne palidron")
        quit()
    print("palidron")
