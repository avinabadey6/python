income=int(input("write down your annual income"))
if income<=200000:
    tax=0
elif income>200000 and income<=1000000:
    rate=10
    tax=(income-200000)*0.1
elif income>1000000 and income<=2500000:
    rate=20
    tax=((income-1000000)*0.2)+5000
elif income>2500000:
    rate=50
    tax=((income-2500000)*0.5)+20000
print(tax)