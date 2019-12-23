principal=int(input("enter the principal amount"))
time=int(input("enter the time"))
if time<=1:
    rate=5
elif time>1 and time<=2:
    rate=6.5
elif time>2 and time<=3:
    rate=7.5
elif time>3 and time<=4:
    rate=8.5
elif time>4:
    rate=10
maturity=principal*(1+rate/100)**time
print(maturity)