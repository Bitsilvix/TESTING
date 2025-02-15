hgt=int(input("Высота "))
rds=int(input("Радиус "))
def cylinder():
    SoCirc=0
    def circle():
        global SoCirc
        SoCirc=3.14*rds**2
    SoSideoCyl=2*3.14*rds*hgt
    inp=input("вычислять только бок или всё?")
    if inp=="1":
        print ("Вычисление бока...")
        print (SoSideoCyl)
    elif inp=="2":
        circle()
        print ("Вычисление всей фигуры...")
        SoCyl=SoSideoCyl+ 2*SoCirc 
        print (SoCyl)
cylinder()