import random

class STUDENT:
    def __init__(self, name, grade, student_id=None):
        self.name = name  # instance variables
        self.grade = grade
        # if no student_id given, assign a random 6-digit number
        self.student_id = student_id if student_id else str(random.randint(100000, 999999))

    def display(self):
        print(f"Name: {self.name}\nGrade: {self.grade}\nStudent ID: {self.student_id}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been successfully updated to {self.grade}")

    def update_id(self):
        self.student_id = str(random.randint(100000, 999999))  # random new ID
        print(f"{self.name}'s ID has been successfully updated to {self.student_id}")


student1 = STUDENT("AARON SINHA", "10th")
student2 = STUDENT("AARON ROY", "11th")
student3 = STUDENT("AARON JR", "12th")

student1.display()
student2.display()
student3.display()

student3.update_grade("University or College")
student3.display()

student3.update_id()
student3.display()
