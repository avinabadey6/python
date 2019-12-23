def name():
    print("hello bro")


name()
def func():
    return 4242
# print(func())
x=func()
print(x)
def reverse():
    b=int(input("enter  numbers"))
    rev=0
    while b!=0:
        c=b%10
        rev=rev*10+c
        b=b//10
    return rev
print(reverse())
def sqr(n):
    s=n*n
    return s
x=sqr(3)
y=sqr(4)
print(x)
print(y)
# def name():
#     a=int(input("enter a number")
#     if a starts with"-":
#         # print("this is negative number")
#     elif a strats with"+":
#         print("this is positive number")
#     elif a=0:
#         print("the value is 0")
# print(a)
def cube(q):
    q=q**3
    print(q)
cube(int(input("input a number")))