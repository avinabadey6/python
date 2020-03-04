filename="avi.txt"
with open(filename,"w") as f:#f is file handler
    f.write("Tapas Pal is no more")

filename2="deba.txt"
f2=open(filename2,"w")
f2.write("Tapas Pal mara ge6en")
f2.close()

with open(filename,"r") as f3:
    print(f3.read())

with open(filename,"a") as f4:
    f4.write("It is very sad news")
