buddies={"name":"Avivai","account_number":23453737378948,"ph_number":8676459875686}
print(buddies)
for t in buddies:
    print(t,"=",buddies[t])
print(buddies["account_number"])
buddies["name"]="salluraj"
print(buddies)
for n in buddies:
    print(n,"-",buddies[n])
print()
red=input("enter the name")
blue=int(input("enter a number"))
green={"name":red,"phone_number":blue}
print(green)
s={}
arrow="abcdefghijklmnopqrstuvwxyz"
num=1
for u in arrow:
    s[u]=num
    num+=1
print(s)