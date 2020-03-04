stocks=[]
items=[]
for i in range(2):
    id=input("enter the id")
    price=float(input("enter the value"))
    name=input("enter the name")
    item={"id":id,"price":price,"name":name}
    items.append(item)
print(items)
ids=[i["id"]for i in items]
print(ids)
for id in ids:
    quantity=int(input("enter the quantity"))
    stocks={'id':id,'quantity':quantity}
assets=0
for items in items:
    assets=item["price"]