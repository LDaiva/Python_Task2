class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            # course.add_student(self)
        return self.enrolled_courses

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = []
            self.grades[course].append(grade)
        return self.grades

    def performance_report(self):
        for course in self.enrolled_courses:
            course_grade = self.grades.get(course)
            print(f"Student: {self.name}, Course: {course}, Grade: {course_grade}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.subject = subject
        self.courses = []

    def list_courses(self, course):
        if course not in self.courses:
            self.courses.append(course)
        return self.courses


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lessons = []
        self.details = {}

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []
            # return f"List of the students: {self.students} List of attendance: {self.attendance}"

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append(date)
            self.attendance[student].append(status)
        return self.attendance

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student)
            attendance_date = attendance_record[0]
            attendance_status = attendance_record[1]
            print(f"Student: {student}, Attendance: {attendance_date}: {attendance_status}")

    def add_lesson(self, lesson):
        if lesson not in self.lessons:
            self.lessons.append(lesson)
            self.details[lesson] = [lesson.date, lesson.material]
        return f"List of the lessons: {self.lessons}, list of the lesson details: {self.details}"

    def get_lessons(self):
        i = 0
        for lesson in self.lessons:
            i += 1
            lesson_details = self.details.get(lesson)
            lesson_date = lesson_details[0]
            lesson_materials = lesson_details[1]
            print(f"{i} lesson: {lesson_date}, {lesson.topic}: {lesson_materials}")


class Lesson:
    def __init__(self, topic, date, material):
        self.topic = topic
        self.date = date
        self.material = material
        # self.materials = []

    # def add_material(self, material):
    #     if material not in self.materials:
    #         self.materials.append(material)
    #     return  f"List of the lesson materials: {self.materials}"


math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher.name)

alice = Student("Alice", 20)
bob = Student("Bob", 21)

# Ar teisinga trumpinti kodą kviečiant funkciją tiesiai print'e?
print(f" {math_teacher.list_courses(math_course.name)} course taught by Teacher {math_teacher.name}")
print(f"The teacher of the {math_course.name} course {math_course.teacher}")

math_course.add_student(alice.name)
math_course.add_student(bob.name)
# print(f" {math_course.add_student(alice.name)} {math_course.add_student(bob.name)}")


print(alice.name, alice.enroll(math_course.name))
print(bob.name, bob.enroll(math_course.name))

# Recording attendance
math_course.record_attendance(alice.name, "2024-09-11", "Present")
math_course.record_attendance(bob.name, '2024-09-11', 'Absent')
print(f"Attendance: {math_course.attendance}")

# Recording grades
print(alice.name, alice.record_grade(math_course.name, "A"))
print(bob.name, bob.record_grade(math_course.name, "B"))

# Generating reports
# Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']
print(math_course.generate_report())

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
bob.performance_report()


lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])


# print(lesson1.topic, lesson1.date, lesson1.add_material("Algebra Textbook Chapter 1"))
# print(lesson2.topic, lesson2.date, lesson2.add_material("Geometry Workbook"))

math_course.add_lesson(lesson1)
math_course.add_lesson(lesson2)

# kodėl apačioje užkomentuotas printas kelis kartus išspausdina objektus???
# print(math_course.add_lesson(lesson1), math_course.add_lesson(lesson2))

print(math_course.get_lessons())
