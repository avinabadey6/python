def circle_area(r):
    c=3.14*r**2
    print(c)

def circle_perimeter(r):
    v=2*3.14*r
    print(v)

def sphere_area(r):
    u=4*3.14*r**2
    print(u)

def sphere_volume(r):
    y=4/3*3.14*r**3
    print(y)

radius=int(input("enter the value of r"))
cs=(input("enter the value"))
if cs=="c":
    circle_perimeter(radius)
    circle_area(radius)
else:
    sphere_area(radius)
    sphere_volume(radius)
