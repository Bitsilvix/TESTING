anskey1=0
anskey2=0
anskey3=0
anskey4=0
anskey5=0
anskey6=0
print ("Hello, this is a quiz, if you win - you're got a 100.000$")
print ("First question: What the coolest project on Telegram?")
print ("1. Hamster Combat")
print ("2. X Empire")
print ("3. Tomato Market")
print ("4. Lost Dogs")
print ("5. Blum")
print ("6. CATS")
print ("1284920. Mouse Brawl")
a = str(input("Answer:"))
if a=='7' or a=='1284920':
    print ("Alright! That's right!")
    anskey1 = 1
else:
    print ("NOT, try again please.")
if anskey1 == 1:
    print ("Second question: What the best currency?")
    print ("1. Bitcoin")
    print ("2. Ethereum")
    print ("3. Litecoin")
    print ("4. TON")
    print ("5. $HMSTR")
    b = str(input())
    if b=='5':
        print ("Alright! That's right!")
        anskey2 = 1
    else:
        print ("NOT, try again please.")
if anskey2 == 1:
    print ("Third question: What the best program?")
    print ("1. Bin")
    print ("2. CMD")
    print ("3. Hard drive(C:)")
    print ("4. TROJAN.EXE")
    print ("5. Internet Explorer")
    c = str(input())
    if c=='4':
        print ("Alright! That's right!")
        anskey3 = 1
    else:
        print ("NOT, try again please.")
if anskey3 == 1:
    print ("Fourth question: What the best drink?")
    print ("1. Water")
    print ("2. Fruit Juice")
    print ("3. Shcola without SH")
    print ("4. Coffee")
    print ("5. Tea")
    d = str(input("Answer:"))
    if d=='3':
        print ("Alright! That's right!")
        anskey4 = 1
    else:
        print ("NOT, try again please.")
if anskey4 == 1:
    print ("Fifth question: What the best system?")
    print ("1. Win 10")
    print ("2. Win 7")
    print ("3. Linux")
    print ("4. Mac OS")
    print ("5. Win 8.1")
    print ("6. Win 95")
    e = str(input())
    if e=='6':
        print ("Alright! That's right!")
        anskey5 = 1
    else:
        print ("NOT, try again please.")
if anskey5 == 1:
    print ("Sixth question: What the best game?")
    print ("1. Genshin Impact")
    print ("2. Purble Place")
    print ("3. Dota 2")
    print ("4. CS2")
    print ("5. PUBG")
    print ("6. Zenless Zone Zero")
    print ("7. Minecraft")
    print ("8. Terraria")
    f = str(input())
    if f=='2':
        print ("Alright! That's right!")
        anskey6 = 1
    else:
        print ("NOT, try again please.")
if anskey6 == 1:
    print ("YOU WIN! CONGRATULATIONS!")