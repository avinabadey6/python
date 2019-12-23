money=int(input("enter the total ammount"))
time=int(input("enter your time"))
if time<=1:
    rate=3
elif time>1 and time<=2:
    rate=5
elif time>2 and time<=3:
    rate=7
elif time>3 and time<=4:
    rate=9
elif time>4 and time<=5:
    rate=10
finalresult=money*(1+rate/100)**time 
print(finalresult)
