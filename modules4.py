import random 
code=random.randint(0,1000000000000000000000000)
print("the otp is", code)
otp=int(input("enter the otp here"))
if otp==code:
    print("your otp is correct")
else:
    print("your otp id in-correct")