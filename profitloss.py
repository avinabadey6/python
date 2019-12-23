x=int(input("enter the cp value"))
y=int(input("enter the sp value"))
def profit(cp,sp):
    p=sp-cp
    print("the profit is",p)
    pp=p/cp*100
    print(f"the profit persentenge is {pp}%")
def loss(cp,sp):
    l=cp-sp
    print("the loss is",l)
    lp=l/cp*100
    print(F"the loss pesentenge is {lp}%")
if x<y:
    profit(x,y)
elif x>y:
    loss(x,y)
else:
    print("no profit no loss")

    

