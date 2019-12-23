rio={"Shirsha","Avinaba","Anita","Sreya","Sangita","Debanjan"}
name=input("enter the name of customer")
count=0
for element in rio:
    if name==element:
        count=count+1
if count==1:
    print("The name is in the list")
else:
    print("the name is not in the list")
    