firstnumber=int(input("enter the first number"))
secondnumber=int(input("enter the second number"))
print("press+ for addition,press- for substraction,press* for multiplication,press/ for division,press** for power,press% for remainder")
yoyo=(input())
if yoyo=="+":
    print("the result is",firstnumber+secondnumber)
elif yoyo=="-":
    print("the result is",firstnumber-secondnumber)
elif yoyo=="*":
    print("the result is",firstnumber*secondnumber)
elif yoyo=="/":
    print("the result is",firstnumber/secondnumber)
elif yoyo=="**":
    print("the result is",firstnumber**secondnumber)
elif yoyo=="%":
    print("the result is",firstnumber%secondnumber)