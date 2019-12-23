i=0
while(i<51):
    print("Shisha")
    i=i+1
for i in range(0,51):
    print("Avinaba")
n=int(input("enter the number"))
count=0
while n!=0:
    count=count+1
    n=n//10
print("your number is carrying",count,"digits")
p=int(input("enter the number"))
sum=0
while p!=0:
    sum+=p%10
    p//=10
print(sum)
t=int(input("plz enter a number as u wish"))
sum=0
while t!=0:
    sum+=t%10
    t//=10
print(sum)

