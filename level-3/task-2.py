name=input("Enter your name: ")
age=int(input("Enter your age: "))
course=input("Enter your course: ")

student={
    "name":name,
    "age":age,
    "course":course,
}

with open("student_data.txt", "w") as f:
    for key, value in student.items():
        f.write(f"{key}: {value}\n")

with open("student_data.txt", "r") as f:
    print("\n student details are : ")
    for line in f:
        print(line.strip())
   