# main.py

from operations import *
from sqlalchemy.orm import sessionmaker
from models import Base, engine

Session = sessionmaker(bind=engine)
session = Session()

def run():
    Base.metadata.create_all(engine)

    while True:
        print("\nWelcome to Student Information System")
        print("---------------------------------------")
        print("Please choose an option:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Add/Update Grade")
        print("5. Delete Grade")
        print("6. Get Student Grades")
        print("0. Exit")
        print("---------------------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            student_number = getId()

            departments = load_departments()
            department = select_department(departments)

            add_student(session, first_name, last_name, student_number, department)

            print("Student added successfully")

        elif choice == '2':
            student_id = int(input("Enter student ID to update: "))
            field = input("Enter field to update (first_name, last_name, student_number, department): ")
            value = input(f"Enter new value for {field}: ")
            update_student(session, student_id, **{field: value})
            print("Student updated successfully.\n")

        elif choice == '3':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(session, student_id)
            print("Student deleted successfully\n")

        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            lesson_id = int(input("Enter lesson ID: "))
            grade = input("Enter grade: ")
            add_or_update_grade(student_id, lesson_id, grade)

        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            lesson_id = int(input("Enter lesson ID: "))
            delete_grade(student_id, lesson_id)

        elif choice == '6':
            student_id = int(input("Enter student ID: "))
            get_student_grades(session, student_id)

        elif choice == '0':
            print("Exiting the system...\n")
            break

        else:
            print("Invalid choice. Please try again!\n")

if __name__ == "__main__":
    run()
