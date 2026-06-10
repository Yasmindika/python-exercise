import json
import os

class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number


class Student(Person):
    def __init__(self, student_id, name, email, phone_number):
        super().__init__(name, email, phone_number)
        self.student_id = student_id

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }

    def __str__(self):
        return (
            f"\nStudent ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone_number}\n"
        )


class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = capacity

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "trainer_name": self.trainer_name,
            "capacity": self.capacity
        }

    def __str__(self):
        return (
            f"\nCourse ID: {self.course_id}\n"
            f"Course Name: {self.course_name}\n"
            f"Trainer: {self.trainer_name}\n"
            f"Capacity: {self.capacity}\n"
        )


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []


    def add_student(self):
        student_id = input("Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return

        name = input("Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone Number: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        if "@" not in email:
            print("Invalid email.")
            return

        if not phone:
            print("Phone number cannot be empty.")
            return

        student = Student(student_id, name, email, phone)
        self.students.append(student)

        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(student)

    def search_student(self):
        search = input("Enter Student ID or Name: ").strip().lower()

        found = False

        for student in self.students:
            if (
                student.student_id.lower() == search
                or student.name.lower() == search
            ):
                print(student)
                found = True

        if not found:
            print("Student not found.")

    def add_course(self):
        course_id = input("Course ID: ").strip()

        if not course_id:
            print("Course ID cannot be empty.")
            return

        for course in self.courses:
            if course.course_id == course_id:
                print("Course ID already exists.")
                return

        course_name = input("Course Name: ").strip()
        trainer = input("Trainer Name: ").strip()

        try:
            capacity = int(input("Capacity: "))
        except ValueError:
            print("Capacity must be a number.")
            return

        if capacity <= 0:
            print("Capacity must be greater than 0.")
            return

        course = Course(course_id, course_name, trainer, capacity)
        self.courses.append(course)

        print("Course added successfully.")

    def view_courses(self):
        if not self.courses:
            print("No courses found.")
            return

        for course in self.courses:
            print(course)

    def register_student(self):
        student_id = input("Student ID: ").strip()
        course_id = input("Course ID: ").strip()

        student = None
        course = None

        for s in self.students:
            if s.student_id == student_id:
                student = s
                break

        for c in self.courses:
            if c.course_id == course_id:
                course = c
                break

        if student is None:
            print("Student not found.")
            return

        if course is None:
            print("Course not found.")
            return

        for registration in self.registrations:
            if (
                registration["student_id"] == student_id
                and registration["course_id"] == course_id
            ):
                print(
                    f"{student.name} is already registered for this course."
                )
                return

        count = 0

        for registration in self.registrations:
            if registration["course_id"] == course_id:
                count += 1

        if count >= course.capacity:
            print("Registration failed. This course is already full.")
            return

        self.registrations.append({
            "student_id": student_id,
            "course_id": course_id
        })

        print(
            f"{student.name} successfully registered for "
            f"{course.course_name}."
        )

    def view_students_in_course(self):
        course_id = input("Enter Course ID: ").strip()

        found = False

        for registration in self.registrations:
            if registration["course_id"] == course_id:

                for student in self.students:
                    if (
                        student.student_id
                        == registration["student_id"]
                    ):
                        print(student)
                        found = True

        if not found:
            print("No students registered in this course.")

    def view_courses_for_student(self):
        student_id = input("Enter Student ID: ").strip()

        found = False

        for registration in self.registrations:
            if registration["student_id"] == student_id:

                for course in self.courses:
                    if (
                        course.course_id
                        == registration["course_id"]
                    ):
                        print(course)
                        found = True

        if not found:
            print("Student has not registered for any course.")

    def save_data(self):
        with open("students.json", "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

        with open("courses.json", "w") as file:
            json.dump(
                [course.to_dict() for course in self.courses],
                file,
                indent=4
            )

        with open("registrations.json", "w") as file:
            json.dump(
                self.registrations,
                file,
                indent=4
            )

        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists("students.json"):
            with open("students.json", "r") as file:
                data = json.load(file)

                for item in data:
                    self.students.append(
                        Student(
                            item["student_id"],
                            item["name"],
                            item["email"],
                            item["phone_number"]
                        )
                    )

        if os.path.exists("courses.json"):
            with open("courses.json", "r") as file:
                data = json.load(file)

                for item in data:
                    self.courses.append(
                        Course(
                            item["course_id"],
                            item["course_name"],
                            item["trainer_name"],
                            item["capacity"]
                        )
                    )

        if os.path.exists("registrations.json"):
            with open("registrations.json", "r") as file:
                self.registrations = json.load(file)

        print("Data loaded successfully.")

def main():
    system = SchoolSystem()

    try:
        system.load_data()
    except:
        pass

    while True:
        print("\n===== Student Course Registration System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Register Student to Course")
        print("7. View Students in a Course")
        print("8. View Courses for a Student")
        print("9. Save Data")
        print("10. Load Data")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            system.search_student()

        elif choice == "4":
            system.add_course()

        elif choice == "5":
            system.view_courses()

        elif choice == "6":
            system.register_student()

        elif choice == "7":
            system.view_students_in_course()

        elif choice == "8":
            system.view_courses_for_student()

        elif choice == "9":
            system.save_data()

        elif choice == "10":
            system.load_data()

        elif choice == "0":
            system.save_data()
            print("Goodbye.")
            break

        else:
            print("Invalid option. Try again.")

main()