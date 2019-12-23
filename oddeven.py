x=1
while x<=100:
    # print(x)
    x=x+2
y=0
while y<=100:
    print(y)
    y=y+2 
p=0
while p<=50:
    if p%2==0:
        print(p,"-even")
    else:
        print(p,"-odd")
    p=p+1
l=0
while l<=100:
    if l%2==1:
        print(l,"-odd")
    else:
        print(l,"-even")
    l=l+1
for r in range(1,101):
    if r%2==0:
        r=r**2
        print(r,"even")
    else:
        r=r**3
        print(r,"odd")
for z in range(1,51):
    if z%2==0:
        print(z,"-even")
    else:
        print(z,"-odd")
