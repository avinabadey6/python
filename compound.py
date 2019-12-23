principal=int(input("enter the principal amount"))
time=int(input("enter your time"))
if time<=1:
    rate=5
elif time>1 and time<=2:
    rate=6.5
elif time>2 and time<=3:
    rate=7.5
elif time>3:
    rate=8.5
malurity=principal*(1+rate/100)**time
print(malurity)
givenammount=int(input("enter the ammount"))
timepreiod=int(input("what is time?"))
if time<=1:
    rate=5
elif time>1 and time<=2:
    rate=6.5
elif time>2 and time<=3:
    rate=7.5
elif time>3:
    rate=8
maturity=givenammount*(1+rate/100)**timepreiod
print(maturity)