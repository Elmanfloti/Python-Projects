
class Student:
    
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def status(self):
        print(f"{self.name} has {self.age} years old and he got {self.grade} grades ")
    def get_letter(self):
        if self.grade >= 80 :
            print("A")
        elif self.grade >=60 :
            print("B")
        elif self.grade >= 40 :
            print("C")
        elif self.grade >= 20 :
            print("D")
        elif self.grade >=0 :
            print("F")

students = []

add_more = "yes"
while add_more == "yes":
    name = input("Enter student name: ")
    try:

        age = int(input("Enter student age: "))
    
        grade = int(input("Enter student grade: "))
        students.append(Student(name, age, grade))
        
    except ValueError:

        print("Please enter a valid number ")

    add_more = input("Add another? yes/no: ")


student=Student(name, age, grade)
for student in students:
    student.status()
    student.get_letter()

def tiers():
    grades= [s.grade for s in students]
    highest= max(grades)
    average= sum(grades) / len(grades)
    lowest=min(grades)
    print(f"the highest get {highest}")
    print(f"the average get {average}")
    print(f"the highest get {lowest}")

tiers()

with open("students.txt", "w") as file:
    for student in students:
        file.write(f"{student.name} has {student.age} years old and got {student.grade}\n")