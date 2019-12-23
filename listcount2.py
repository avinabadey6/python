rock={"Sangita","Diganta","Debdut","Rubi"}
names=input("enter the name of the students")
count=0
for element in rock:
    if names==element:
        count=count+1
if count==1:
    print("this is listed name")
else:
    print("this is not listed name")