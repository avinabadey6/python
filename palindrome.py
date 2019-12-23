u=int(input("enter a number"))
n=0
while u!=0:
    r=(u%10)
    n=n*10+r
    u=u//10
    print(u,r,n)
print(n)
# x=1
# while x<11:
#     print(x,end=",")
#     x=x+1
# print()
# n=0
# while n<4:
#     r=n*n
#     n=n+1
# print(r,n)
if u==n:
    print("it is palindrome number")
else:
    print("it is not palindrome number")