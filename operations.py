# operations.py

import json
from models import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def add_student(session, first_name, last_name, student_number, department):
    new_student = Student(
        first_name=first_name,
        last_name=last_name,
        student_number=student_number,
        department=department
    )
    session.add(new_student)
    session.commit()

def update_student(session, student_id, **kwargs):
    student = session.query(Student).filter(Student.id == student_id).first()
    for key, value in kwargs.items():
        setattr(student, key, value)
    session.commit()

def delete_student(session, student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()


def get_student_grades(session, student_id):
    grades = session.query(Grade).filter(Grade.student_id == student_id).all()
    for grade in grades:
        lesson = session.query(Lesson).filter(Lesson.id == grade.lesson_id).first()
        print(f"Lesson: {lesson.lesson_name}, Not: {grade.grade}")

def getId():
    while True:
        try:
            student_number = input("Enter student number: ")
            if len(student_number) != 9 or not student_number.isdigit():
                raise ValueError("Student number must be a 9-digit number.")
            return int(student_number)
        except ValueError as e:
            print(e)

def load_departments(filename='departments.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        departments = json.load(f)
    print("Departments successfully loaded.")
    return departments

def select_department(departments):
    departments = load_departments()

    print("Fakülteler:")
    faculties = list(departments.keys())
    for index, faculty in enumerate(faculties, start=1):
        print(f"{index}. {faculty}")

    faculty_choice = int(input("Fakülte numarasını seçin: ")) - 1
    selected_faculty = faculties[faculty_choice]
    print(f"\n{selected_faculty} Bölümleri:")

    faculty_departments = departments[selected_faculty]
    for index, department in enumerate(faculty_departments, start=1):
        print(f"{index}. {department}")

    department_choice = int(input("Bölüm numarasını seçin: ")) - 1
    selected_department = faculty_departments[department_choice]
    return selected_department



def add_or_update_grade(student_id, lesson_id, grade):
    session = Session()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        lesson = session.query(Lesson).filter(Lesson.id == lesson_id).first()

        if not student:
            print("Student not found!\n")
            return
        if not lesson:
            print("Lesson not found!\n")
            return

        existing_grade = session.query(Grade).filter(Grade.student_id == student_id,
                                                     Grade.lesson_id == lesson_id).first()

        if existing_grade:
            existing_grade.grade = grade
            print("Grade updated successfully.\n")
        else:
            new_grade = Grade(student_id=student_id, lesson_id=lesson_id, grade=grade)
            session.add(new_grade)
            print("Grade added successfully.\n")

        session.commit()

    finally:
        session.close()


def delete_grade(student_id, lesson_id):
    session = Session()
    try:
        grade = session.query(Grade).filter(Grade.student_id == student_id, Grade.lesson_id == lesson_id).first()
        if grade:
            session.delete(grade)
            session.commit()
            print("Grade deleted successfully.\n")
        else:
            print("Grade not found!\n")

    finally:
        session.close()

def load_lessons(json_file_path='lessons.json'):
    session = Session()
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for period, lessons in data.items():
        for lesson_code, lesson_name in lessons.items():
            if not session.query(Lesson).filter_by(lesson_code=lesson_code).first():
                new_lesson = Lesson(lesson_name=lesson_name, lesson_code=lesson_code)
                session.add(new_lesson)

    session.commit()
    session.close()
    print("Lessons successfully loaded.")


