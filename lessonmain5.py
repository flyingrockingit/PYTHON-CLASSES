class Person:
    def __init__(self, name, email, id_number):
        self.name = name
        self.email = email
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nID: {self.id_number}")


class Student(Person):
    def __init__(self, name, email, id_number, grade, subject):
        super().__init__(name, email, id_number)
        self.grade = grade
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade}\nSubject: {self.subject}")


class Teacher(Person):
    def __init__(self, name, email, id_number, department, course):
        super().__init__(name, email, id_number)
        self.department = department
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}\nCourse: {self.course}")


class RegistrationSystem:
    def __init__(self):
        self.students = []
        self.teachers = []

    def register_student(self, name, email, id_number, grade, subject):
        student = Student(name, email, id_number, grade, subject)
        self.students.append(student)
        print("Student registered successfully.✅")

    def register_teacher(self, name, email, id_number, department, course):
        teacher = Teacher(name, email, id_number, department, course)
        self.teachers.append(teacher)
        print("Teacher registered successfully.✅")

    def display_all_students(self):
        print("\nRegistered Students:")
        for student in self.students:
            student.display_info()
            print("------------")

    def display_all_teachers(self):
        print("\nRegistered Teachers:")
        for teacher in self.teachers:
            teacher.display_info()
            print("------------")

system=RegistrationSystem()

system.register_student("Bob", "bob.starely@example.com", "S202", "11th", "Science")

system.register_teacher("Mr. Smith", "smithaar@example.com", "T111", "Math Dept", "Algebra")

system.display_all_students()
system.display_all_teachers()
