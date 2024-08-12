# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///student_db.sqlite3')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment id
    first_name = Column(String)
    last_name = Column(String)
    student_number = Column(Integer, unique=True)
    department = Column(String)
    grades = relationship('Grade', back_populates='student')

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment id
    lesson_name = Column(String)
    lesson_code = Column(String, unique=True)
    grades = relationship('Grade', back_populates='lesson')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment id
    student_id = Column(Integer, ForeignKey('students.id'))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    grade = Column(String)
    student = relationship('Student', back_populates='grades')
    lesson = relationship('Lesson', back_populates='grades')

def setup_database():
    Base.metadata.create_all(engine)
    print("Database successfully created.")