class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)

    def select_course_and_input_marks(self):
        self.list_courses()
        course_id = input("Select a course by ID to input marks: ")
        for student in self.students:
            marks = input(f"Enter marks for {student.name} in {course_id}: ")
            student.add_marks(course_id, marks)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"{course.course_id}: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"{student.student_id}: {student.name} (DOB: {student.dob})")

    def show_student_marks(self):
        course_id = input("Enter course ID to view marks: ")
        print(f"Marks for course {course_id}:")
        for student in self.students:
            marks = student.marks.get(course_id, 'No marks entered')
            print(f"{student.name}: {marks}")


def main():
    school = School()
    school.input_students()
    school.input_courses()
    school.select_course_and_input_marks()
    school.list_students()
    school.show_student_marks()


if __name__ == "__main__":
    main()
