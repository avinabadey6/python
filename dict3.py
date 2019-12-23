fox={"Name":"Avi","Game":"Naba"}
print(fox.keys())
print(fox.values())
print(type(fox.items()))
for u in fox.items():
    print(u)
for u,v in fox.items():
    print(u,v)
fox["Name"]="Avinaba"
print(fox)