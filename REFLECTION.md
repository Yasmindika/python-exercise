# Reflection

## What was the hardest part of this project?

The hardest part was understanding how Object-Oriented Programming works, especially inheritance between the Person and Student classes.

## Which classes did you create and why?

I created these classes:

* **Person**: to store basic details like name, email, and phone number
* **Student**: to store student ID and inherit from Person
* **Course**: to store course details like course ID, name, trainer, and capacity
* **SchoolSystem**: to manage students, courses, and registrations in the system

## How does your registration logic prevent duplicate registrations?

Before adding a registration, the system checks if the student is already registered for that same course. If yes, it does not allow it again.

## How does your system check if a course is full?

The system counts how many students are already registered in a course. If the number reaches the course capacity, it stops new registrations.

## What bugs did you face and how did you fix them?

At first, I had problems with duplicate student IDs and course IDs. I fixed this by checking before adding new ones.

I also had issues with students registering more than once, but I solved it by checking existing registrations.

Sometimes the program also crashed when wrong input was entered, so I added simple validation and try/except for numbers.

## Which part of the code would you improve if you had more time?

If I had more time, I would improve the project by adding delete and update features. I would also make the system easier to use and improve the file handling part.
