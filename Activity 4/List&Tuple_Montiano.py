import json

class StudentRecordManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_file()

    def load_file(self):
        try:
            with open(self.filename, "r") as file:
                self.students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def save_file(self, filename=None):
        if filename:
            self.filename = filename
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def show_all(self):
        for student in self.students:
            print(student)

    def order_by_lastname(self):
        self.students.sort(key=lambda x: x['name'][1])
        self.show_all()

    def order_by_grade(self):
        self.students.sort(key=lambda x: x['final_grade'], reverse=True)
        self.show_all()

    def show_student(self, student_id):
        for student in self.students:
            if student['id'] == student_id:
                print(student)
                return
        print("Student not found.")

    def add_record(self):
        student_id = input("Enter Student ID (6 digits): ")
        name = (input("Enter First Name: "), input("Enter Last Name: "))
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        final_grade = (class_standing * 0.6) + (major_exam * 0.4)
        self.students.append({"id": student_id, "name": name, "class_standing": class_standing, "major_exam": major_exam, "final_grade": final_grade})
        self.save_file()
        print("Student record added successfully.")

    def edit_record(self, student_id):
        for student in self.students:
            if student['id'] == student_id:
                student['class_standing'] = float(input("Enter new Class Standing Grade: "))
                student['major_exam'] = float(input("Enter new Major Exam Grade: "))
                student['final_grade'] = (student['class_standing'] * 0.6) + (student['major_exam'] * 0.4)
                self.save_file()
                print("Record updated successfully.")
                return
        print("Student not found.")

    def delete_record(self, student_id):
        self.students = [student for student in self.students if student['id'] != student_id]
        self.save_file()
        print("Record deleted successfully.")

manager = StudentRecordManager()
while True:
    print("\nMenu:")
    print("1. Show All Students Record")
    print("2. Order by Last Name")
    print("3. Order by Grade")
    print("4. Show Student Record")
    print("5. Add Record")
    print("6. Edit Record")
    print("7. Delete Record")
    print("8. Save File")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        manager.show_all()
    elif choice == "2":
        manager.order_by_lastname()
    elif choice == "3":
        manager.order_by_grade()
    elif choice == "4":
        manager.show_student(input("Enter Student ID: "))
    elif choice == "5":
        manager.add_record()
    elif choice == "6":
        manager.edit_record(input("Enter Student ID to edit: "))
    elif choice == "7":
        manager.delete_record(input("Enter Student ID to delete: "))
    elif choice == "8":
        manager.save_file()
    elif choice == "9":
        break
    else:
        print("Invalid choice. Try again.")
