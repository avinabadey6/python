oppo=[]
print(dir(oppo))
oppo.extend(["sallu","jittu"])
print(oppo)
oppo.append("salman")
oppo.append("bajrang")
print(oppo)
oppo.extend(["jio","polo","toy","hat"])
print(oppo)
oppo.insert(4,"raj")
oppo.insert(-3,"gentle")
print(oppo)
b=oppo.pop()
print(b)
oppo.remove("toy")
print(oppo)
oppo.reverse()
print(oppo)
oppo.sort()
print(oppo)
oppo.sort(reverse=True)
print(oppo)
u=oppo.count("polo")
print("the number is-",u)
