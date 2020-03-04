comment=input("pls write a comment here")
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
for vowels in comment:
    if vowels=="a" or vowels=="A":
        a_count=a_count+1
    if vowels=="e" or vowels=="E":
        e_count=e_count+1
    if vowels=="i" or vowels=="I":
        i_count=i_count+1
    if vowels=="o" or vowels=="O":
        o_count=o_count+1
    if vowels=="u" or vowels=="U":
        u_count=u_count+1
print(comment)
print("a_count:",a_count)
print("e_count:",e_count)
print("i_count:",i_count)
print("o_count:",o_count) 
print("u_count:",u_count)   
