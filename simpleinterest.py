def simpleinterest1(p,r,t):
    print(p+p*r*t/100)
def simpleinterest2(p,t,r=5):
    print(p+p*r*t/100)
x=int(input("entenmthe principal ammount"))
y=int(input("enter the rate"))
z=int(input("enter the time period"))
simpleinterest1(x,y,z) #only arguement
simpleinterest1(x,y,t=z) #1 keyword arg,rest posisitional arg 
simpleinterest1(p=x,t=z,r=y) #all keyword arg

simpleinterest2(x,z,y) 
simpleinterest2(x,z) #without y default parameter value is applied
