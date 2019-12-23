u=0
while(u<11):
    print("Shirsha")
    u=u+1
for t in range(0,11):
    print("Avinaba",end="+Shirsha,")
print()
o=int(input("enter a number"))
count=0
while o!=0:
    count=count+1
    o=o//10
print("your number is carrying",count,"digits")
h=int(input("enter a number"))
sum=0
while h!=0:
    sum+=h%10
    h//=10
print(sum)          
