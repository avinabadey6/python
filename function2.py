def name():
    print("yo yo honey singh")
name()
def news():
    return 488443
print(news())
def bio():
    return "toy is made of plastic"
print(bio())
def hat():
    return "hey r u there or not"
print(hat())
def ribbon():
    return "i am not kidding with you"
x=ribbon()
print(x)
def reverse():
    a=int(input("enter a number what u need"))
    g=0
    while a!=0:
        v=a%10
        g=g*10+v
        a=a//10
    return g
print(reverse())
def addition():
    q=int(input("enter a number"))
    t=0
    while t!=0:
        v=t+q
    return addition
print(reverse())
n=int(input("enter the number"))
def sqr(num):
    print(num*num)
sqr(2)
sqr(n)
rog=int(input("put your name"))
def posneg(r):
    if r>0:
        print("this is positive number")
    elif r<0:
        print("this is negative number")
    elif r==0:
        print("this is zero number")
posneg(rog)
n=int(input("enter the new number"))
largest=n%10
while(n!=0):
    r=n%10
    if r>largest:
        largest=r
    n=n//10
print(largest)

