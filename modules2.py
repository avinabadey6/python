import random
code=random.randint(10,99)
print("your code is", code)
r=int(input("enter the code here"))
if r==code:
    print("your code is correct")
else:
    print("Please re-check your code")
    