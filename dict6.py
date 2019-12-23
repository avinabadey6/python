people={"name":"Avi","roll":5,"subject":"sci"}
# print(people)
for p in people:
    print(people[p])
people["name"]="jhimmy"
for t in people:
    print(t,"-",people[t],end=",")
print()
id=input("enter your name")
num=int(input("enter the number"))
user={"name":id,"score":num}
print(user)