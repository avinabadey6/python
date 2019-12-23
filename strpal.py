x="madam"
print(len(x))
y=list(x)
y.reverse()
print(y)
# print(str(y))cannot possible
z="".join(y)
print(z)
if x==z:
    print("palindrome")
else:
    print("it does not palindrome")

