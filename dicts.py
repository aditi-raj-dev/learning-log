#creation
student={
    "name":"Aditi",
    "age":20,
    "cgpa":8.86
}

#access
print(student["name"])

#update
student["age"]=21
student["branch"]="CSE"

#looping
for key,value in student.items():
    print(key,value)

#custom examples
marks={"math":85,"science":90}
marks["english"]=88

total=0
for m in marks.values():
    total+=m
print("total:",total)

highest=0
for score in marks.values():
    if score>highest:
        highest=score
print("highest",highest)