import random
f=open("random.txt","w")
for p in range(100000):
    otp=random.randint(100000,999999)
    f.write(str(otp)+" ")
f.close()