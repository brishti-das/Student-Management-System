# Student Management System

## Project Overview
The Student Management System is a Python-based project developed using Object-Oriented Programming (OOP) concepts. It manages student information for different types of students, including General, Undergraduate, and Graduate students.

## Features
- Store student information (Name, Student ID, Email, Age, Department).
- Display student information.
- Calculate average marks.
- Identify different types of students.
- Store semester information for Undergraduate students.
- Store research topics for Graduate students.

## Classes

### 1. Student (Parent Class)
Attributes:
- name
- student_id
- email
- age
- department

Methods:
- `display_info()` – Displays student information.
- `calculate_result()` – Calculates the average marks.
- `get_student_type()` – Returns the student type.
- `get_email()` – Retrieves the private email attribute.

### 2. UndergraduateStudent (Child Class)
- Inherits from the Student class.
- Additional attribute: `semester`.
- Overrides `get_student_type()`.

### 3. GraduateStudent (Child Class)
- Inherits from the Student class.
- Additional attribute: `research_topic`.
- Overrides `get_student_type()`.

## OOP Concepts Used
- **Class & Object:** Creating classes and their objects.
- **Attributes & Methods:** Managing student data and operations.
- **Inheritance:** Reusing properties and methods from the parent class.
- **Polymorphism:** Using the same method with different behaviors.
- **Method Overriding:** Redefining parent class methods in child classes.
- **Method Overloading:** Using `*args` to accept different numbers of marks.
- **Encapsulation:** Using a private email attribute (`__email`).

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)


## Author
**Brishti Das**

