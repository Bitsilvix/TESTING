def rectangle():
    a =int(input())
    b =int(input())
    print("The square of rect equal to", a*b)
def triangle():
    a =int(input())
    h =int(input())
    print("The square of triangle equal to", 0.5*h*a)
def circle():
    r =int(input())
    print("The square of circle equal to", 3.14*r**2)
figure=input("1-rect,2-triangle,3-circle")
if figure=='1':
    rectangle()
elif figure=='2':
    triangle()
elif figure=='3':
    circle()
else:
    print("Error")
