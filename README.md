# Student Course Registration System

## What the Project Does

This project is a command-line Python application that helps a training school manage students, courses, and course registrations.

The system allows an administrator to:

* Add students
* Add courses
* Register students to courses
* View students
* View courses
* Search for students
* Save and load data from files

---

## How to Run the Project

1. Make sure Python is installed on your computer.
2. Open the project folder in the terminal.
3. Run the following command:

```bash
python3 work.py
```

4. Follow the menu options displayed on the screen.

---

## Features Implemented

* Add a new student
* View all students
* Search for a student by ID or name
* Add a new course
* View all courses
* Register a student to a course
* Prevent duplicate student IDs
* Prevent duplicate course IDs
* Prevent duplicate registrations
* Prevent registration when a course is full
* Save data using JSON files
* Load saved data when the application starts
* Input validation and error handling

---

## Classes Used

### Person

A base class that stores:

* Name
* Email
* Phone number

### Student

Inherits from the Person class and stores:

* Student ID
* Name
* Email
* Phone number

### Course

Stores:

* Course ID
* Course Name
* Trainer Name
* Capacity

### SchoolSystem

Handles the main functionality of the application, including:

* Student management
* Course management
* Registrations
* Saving and loading data

---

## Challenges Faced

Some challenges faced during this project included:

* Implementing inheritance using the Person and Student classes
* Preventing duplicate student and course records
* Managing student registrations
* Handling course capacity limits
* Saving and loading data using JSON files
* Validating user input and preventing program crashes

This project helped me understand object-oriented programming, file handling, validation, and error handling in Python.
