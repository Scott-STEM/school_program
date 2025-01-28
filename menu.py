"""Initializes the program and allows the user to
choose between students and subjects and classes."""
import students
import sch_class

def choose_action():
    """Gets the user to choose between subjects or students."""
    while True:
        user_action = input("Please type either 'classes', 'students' or 'subjects' or 'exit': ").lower()
        if user_action == "students":
            students.student_del_ins()  # Referencing from the students module
        elif user_action == "subjects":
            subjects.in_del_sub()  # Referencing from the subjects module
        elif user_action == "classes":
            sch_class.class_menu()
        elif user_action == "exit":
            return
        else:
            print("Invalid choice, please try again.")

choose_action()
