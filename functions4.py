import json
student = {
"name": "Rahul",
"age" : 21,
"Course" :"Python",
"marks" : 85
}
with open("student.json","w") as f:
    json.dump(student,f,indent=4)
with open("student.json","r") as f:
    student= json.load(f)
print(student)