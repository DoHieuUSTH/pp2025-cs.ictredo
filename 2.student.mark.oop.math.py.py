class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def add_marks(self, course_id, marks):
        self.__marks[course_id] = marks

    def get_marks(self, course_id):
        return self.__marks.get(course_id, 'No marks entered')

    def __str__(self):
        return f"{self.__student_id}: {self.__name} (DOB: {self.__dob})"


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def __str__(self):
        return f"{self.__course_id}: {self.__name}"


class School:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            student = Student(student_id, name, dob)
            self.__students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.__courses.append(course)

    def input_marks(self):
        self.list_courses()
        course_id = input("Select a course by ID to input marks: ")
        for student in self.__students:
            marks = input(f"Enter marks for {student} in {course_id}: ")
            student.add_marks(course_id, marks)

    def list_courses(self):
        print("Courses:")
        for course in self.__courses:
            print(course)

    def list_students(self):
        print("Students:")
        for student in self.__students:
            print(student)

    def show_student_marks(self):
        course_id = input("Enter course ID to view marks: ")
        print(f"Marks for course {course_id}:")
        for student in self.__students:
            marks = student.get_marks(course_id)
            print(f"{student.__str__()}: {marks}")


def main():
    school = School()
    school.input_students()
    school.input_courses()
    school.input_marks()
    school.list_students()
    school.show_student_marks()


if __name__ == "__main__":
    main()