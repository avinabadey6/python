def simint1(p,r,t):
    print(p+p*r*t/100)
def simint2(p,t,r=4):
    print(p+p*r*t/100)
    
a=int(input("enter the principal amount"))
b=int(input("enter the rate of money"))
c=int(input("enter the time"))
simint1(a,b,c)
simint1(p=a,r=b,t=c)
simint1(a,b,t=c)

simint2(a,b,c)
simint2(a,c)