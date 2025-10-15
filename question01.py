class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print("No students found.")
        else:
            for student in cls.student_list:
                student.view_student_info()


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self._is_enrolled:
            print(f"{self._name} is already enrolled!")
        else:
            self._is_enrolled = True
            print(f"{self._name} has been successfully enrolled!")

    def drop_student(self):
        if not self._is_enrolled:
            print(f"{self._name} is not enrolled, cannot drop!")
        else:
            self._is_enrolled = False
            print(f"{self._name} has been successfully dropped!")

    def view_student_info(self):
        print("-------------------------------")
        print(f"Student ID : {self._student_id}")
        print(f"Name       : {self._name}")
        print(f"Department : {self._department}")
        print(f"Enrolled   : {'Yes' if self._is_enrolled else 'No'}")

    def get_id(self):
        return self._student_id


s1 = Student(101, "Sadia Rahman", "CSE", True)
s2 = Student(102, "Rafiq Islam", "EEE")
s3 = Student(103, "Sabbir Ahmed", "BBA")


while True:
    print("\n===== Student Database Menu =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            StudentDatabase.view_all_students()

        elif choice == 2:
            student_id = int(input("Enter Student ID to enroll: "))
            found = False
            for stu in StudentDatabase.student_list:
                if stu.get_id() == student_id:
                    stu.enroll_student()
                    found = True
                    break
            if not found:
                print("Invalid Student ID!")

        elif choice == 3:
            student_id = int(input("Enter Student ID to drop: "))
            found = False
            for stu in StudentDatabase.student_list:
                if stu.get_id() == student_id:
                    stu.drop_student()
                    found = True
                    break
            if not found:
                print("Invalid Student ID!")

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select from 1 to 4.")

    except ValueError:
        print("Error: Please enter a valid number.")
