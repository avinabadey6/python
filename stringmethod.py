name="Subhas Saren WICKET! TIMBER! Chopped on by Elgar and it looks like South Africa are going to collapse here. Length ball just outside off, Elgar is caught in two minds whether to play at it or not. Gets an inside edge onto the pads which goes onto rattle the stumps."
# print(dir(name))
print(name.lower())
print(name.upper())
print(name.islower())
print(name.isupper())
print(name.isalpha())
print(name.isalnum())
print(name.capitalize()) #it converts the first letter of the first word of theb string to capital
print(name.title())
print(name.isascii())
print(name.find("subhas")) #it looks for a particular string in same case. It returns either the index number or -1
print(name.count("The")) #it counts the number of times a particular string is present in same case. It returns an integer.
print(name.startswith("Subhas")) #it checks whether a string starts with a particular string or a character. It returns True or False.
withoutunderscore=[]
withunderscore=[]
for i in dir(name):
    if not i.startswith("__"):
        withoutunderscore.append(i)
    else:
        withunderscore.append(i)
print(withunderscore)
        
print(withoutunderscore)
print(len(withoutunderscore))
opo=input("Write the name")
print(opo.endswith("Dey"))
if opo.endswith("Dey"):
    print("u may be my relative")
r="avinabadey86@gmail.com"
w=r.split("@")
print(w)
print(w[0])
y=["oppo","vivo","mi"]
z="_".join(y) #it joins the list elements into a string.
print(z)




# dog="avinaba"
# print(dog.islower())
# print(dog.isupper())
