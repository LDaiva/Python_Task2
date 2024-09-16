class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return self.name, self.age


persons = Person("Jon", 22)
print(persons.show())


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self.name)
            return self.enrolled_courses
    #
    # def performance_report(self):
    #     print(f"Student: N/A, Course: N/A, Grade: N/A")
    #
    # def record_grade(self, course, grade):
    #     if course in self.enrolled_courses:
    #         self.grades[course] = self.grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self, course):
        if course not in self.courses:
            self.courses.append(course)
        return print(course)


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        # teacher.courses.append(self.name)  # Add this course to the teacher's course list

    def get_detales(self):
        return print(f"Teacher: {self.teacher}")

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []
            return self.students

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = "VIRUS VIRUS VIRUS"
            print(f"Student: {student.name}, Attendance: {attendance_status}")


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bobb", 22)
print(math_teacher.name, math_teacher.age, math_teacher.subject)
print(math_teacher.list_courses(math_course))
print(math_course.get_detales())
print(math_course.name, math_teacher.subject, math_teacher.name)
print(math_course.add_student(alice))
print(alice.enroll(math_course))
print(f"Student: {alice.name}, age: {alice.age}, Course: {alice.enroll(math_course)}")
print(f"Name: {bob.name}, age: {bob.age}")
# print(bob.enroll("math_course"))
# print(bob.enroll("english_course"))
