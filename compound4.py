principal=int(input("enter the value"))
time=int(input("enter the time period"))
if time<=1:
    rate=2
elif time>1 and time<=2:
    rate=3
elif time>2 and time<=3:
    rate=4
elif time>3 and time<=4:
    rate=5
elif time>4 and time<=5:
    rate=6
Total_result=principal*(1+rate/100)**time
print(Total_result)