totals=[]
for p in range(2):
    student_id=input("input the id")
    student_roll=input("enter the roll number")
    student_name=input("enter the name")
    students={"student_id":student_id,"student_roll":student_roll,"student_name":student_name}
    totals.append(students)
print(totals)
id_special=[p["student_id"]for p in totals]
print(id_special)
onlynames=[o["student_name"]for o in totals]
print(onlynames)

