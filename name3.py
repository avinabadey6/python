n=int(input("enter your number"))
count=0
while n!=0:
    count=count+1
    n=n//10
print(count)
p=int(input("put any one number"))
sum=0
while p!=0:
    sum=sum+p%10
    p//=10 
print(sum)
