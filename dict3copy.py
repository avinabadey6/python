name={"Name":"Raj","Roll":"avyth"}
print(name.keys())
print(name.values())
print(type(name.items()))
for t in name.items():
    print(t)
for c,b in name.items():
    print(c,b)
name["Name"]="Shaym"
print(name)