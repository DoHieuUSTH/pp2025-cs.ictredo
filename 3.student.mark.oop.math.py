import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__credits = {}

    def add_marks(self, course_id, marks, credits):
        self.__marks[course_id] = marks
        self.__credits[course_id] = credits

    def calculate_gpa(self):
        total_weighted_marks = sum(
            self.__marks[course] * self.__credits[course]
            for course in self.__marks
        )
        total_credits = sum(self.__credits.values())
        return math.floor((total_weighted_marks / total_credits) * 10) / 10 if total_credits else 0

    def __str__(self):
        return f"{self.__student_id}: {self.__name} (DOB: {self.__dob}) - GPA: {self.calculate_gpa()}"


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

    def input_students(self, stdscr):
        stdscr.clear()
        num_students = int(curses.textpad.Textbox(stdscr).edit().strip())
        for _ in range(num_students):
            stdscr.addstr("Enter student ID: ")
            student_id = curses.textpad.Textbox(stdscr).edit().strip()
            stdscr.addstr("Enter student name: ")
            name = curses.textpad.Textbox(stdscr).edit().strip()
            stdscr.addstr("Enter student Date of Birth (YYYY-MM-DD): ")
            dob = curses.textpad.Textbox(stdscr).edit().strip()
            student = Student(student_id, name, dob)
            self.__students.append(student)

    def input_courses(self, stdscr):
        stdscr.clear()
        num_courses = int(curses.textpad.Textbox(stdscr).edit().strip())
        for _ in range(num_courses):
            stdscr.addstr("Enter course ID: ")
            course_id = curses.textpad.Textbox(stdscr).edit().strip()
            stdscr.addstr("Enter course name: ")
            name = curses.textpad.Textbox(stdscr).edit().strip()
            course = Course(course_id, name)
            self.__courses.append(course)

    def input_marks(self, stdscr):
        self.list_courses(stdscr)
        stdscr.addstr("Select a course by ID to input marks: ")
        course_id = curses.textpad.Textbox(stdscr).edit().strip()
        credits = int(curses.textpad.Textbox(stdscr).edit().strip())

        for student in self.__students:
            stdscr.addstr(f"Enter marks for {student} in {course_id}: ")
            marks = float(curses.textpad.Textbox(stdscr).edit().strip())
            marks = math.floor(marks * 10) / 10  # Round down to 1 decimal
            student.add_marks(course_id, marks, credits)

    def list_courses(self, stdscr):
        stdscr.addstr("Courses:\n")
        for course in self.__courses:
            stdscr.addstr(str(course) + "\n")
        stdscr.refresh()

    def list_students(self, stdscr):
        stdscr.addstr("Students:\n")
        sorted_students = sorted(self.__students, key=lambda s: s.calculate_gpa(), reverse=True)
        for student in sorted_students:
            stdscr.addstr(str(student) + "\n")
        stdscr.refresh()

    def show_student_marks(self, stdscr):
        stdscr.addstr("Enter course ID to view marks: ")
        course_id = curses.textpad.Textbox(stdscr).edit().strip()
        stdscr.addstr(f"Marks for course {course_id}:\n")
        for student in self.__students:
            marks = student.get_marks(course_id)
            stdscr.addstr(f"{student}: {marks}\n")
        stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    school = School()

    stdscr.addstr("Input number of students in class:\n")
    school.input_students(stdscr)

    stdscr.addstr("Input number of courses:\n")
    school.input_courses(stdscr)

    school.input_marks(stdscr)

    school.list_students(stdscr)

    stdscr.addstr("Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)