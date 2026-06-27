record=[]
name=input("Enter your name: ")
age=int(input("Enter your age: "))
course=input("Enter your course: ")

student={
    "name":name,
    "age":age,
    "course":course,
}

record.append(student)

print("\n student details are : ")
for i in record:
    print(i["name"])
    print(i["age"])
    print(i["course"])
    print("-"*20)
  