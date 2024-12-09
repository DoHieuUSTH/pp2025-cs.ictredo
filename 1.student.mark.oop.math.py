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
        if num_students.isdigit() and int(num_students) > 0:
            return int(num_students)
        else:
            print("Number of student must be positive!")

        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name_student = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            student = Student(student_id, name, dob)
            self.students.append(student)
            self.marks[student_id] = {}
            print(f"New Student added: {student_name}")

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        if num_courses.isdigit() and int(num_courses) > 0:
            return int(num_courses)
        else:
            print("Number of course must be positive!")

        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name_course = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)
            self.marks[course_id] = {}
            print(f"New Course added: {course_name}")

    def select_course_and_input_marks(self):
        if len(courses) == 0:
           print("Please input course!")
           return
        print("Course list:")
        for c in courses:
            print(f"  {c[0]}: {c[1]}")
        course_id = input("Print ID to type mark: ")
        if course_id not in marks:
           print("Not valid ID!")
           return
        if len(students) == 0:
           print("Please add student name!")
           return
        for s in students:
            while True:
                mark = input(f"Type mark for {s[1]}: ")
                try:
                    mark = float(mark)
                    if 0 <= mark <= 20:
                        marks[course_id][s[0]] = mark
                        break
                    else:
                        print("0 to 20!")
                except:
                    print("Mark must be a number!")

    def list_courses(self):
        if len(course) == 0:
           print("Please print id")
        else:
            print("Course")
        for c in list_courses:
            print(f"  {c[0]}: {c[1]}")
        for course in self.courses:
            print(f"{course.course_id}: {course.name}")

    def list_students(self):
        if len(student) == 0:
        print("Not student yet!")
    else:
        print("Students list:")
        for s in students:
            print(f"  {s[0]}: {s[1]}, DOB: {s[2]}")
        for student in self.students:
            print(f"{student.student_id}: {student.name} (DOB: {student.dob})")

    def show_student_marks(self):
        course_id = input("Enter course ID to view marks: ")
        print(f"Marks for course {course_id}:")
        for student in self.students:
            marks = student.marks.get(course_id, 'No marks entered')
            print(f"{student.name}: {marks}")
        if len(courses) == 0:
           print("Chưa có môn học nào!")
           return
        print("Danh sách môn học:")
        for c in courses:
            print(f"  {c[0]}: {c[1]}")
        course_id = input("Chọn ID môn học để xem điểm: ")
        if course_id not in marks:
           print("ID môn học không hợp lệ!")
           return
        if len(marks[course_id]) == 0:
           print("Chưa có điểm nào cho môn học này!")
        else:
           print(f"Điểm cho môn {course_id}:")
           for stu_id, mark in marks[course_id].items():
               name = next((s[1] for s in students if s[0] == stu_id), "Không rõ")
               print(f"  {name} ({stu_id}): {mark}")


def main():
    school = School()
    school.input_students()
    school.input_courses()
    school.select_course_and_input_marks()
    school.list_students()
    school.show_student_marks()


if __name__ == "__main__":
    main()
