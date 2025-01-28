students_list = []

student_details = [
    {"name": "John Doe", "age": 15},
    {"name": "Jane Smith", "age": 14},
    # Add more students
]

def ask_student_details():
    """Asks the user to input student details."""
    stu_fname = input("What is the student's first name: ")
    stu_lname = input("What is the student's last name: ")
    stu_dob = input("In an 8 letter format (dd/mm/yyyy) enter the student's DOB: ")
    stu_age = int(input("How old is the student? "))

    student_details = {
        "First Name": stu_fname,
        "Surname": stu_lname,
        "Date of Birth": stu_dob,
        "Student's Age": stu_age
    }
    
    students_list.append(student_details)
    print(f"Student {stu_fname} {stu_lname} has been added.")
    return student_details

def delete_student():
    """Deletes a student based on their first name."""
    if not students_list:
        print("No students to delete.")
        return

    del_fname = input("Enter the first name of the student you want to delete: ")
    
    for student in students_list:
        if student["First Name"].lower() == del_fname.lower():
            students_list.remove(student)
            print(f"Student {del_fname} has been deleted.")
            return

    print(f"No student found with the first name {del_fname}.")

def list_students():
    """ Lists the Students in the 'Students_List'"""
    if students_list is not None:
        for student in students_list:
            print(student)
    else:
        print("No students found.")


def student_del_ins():
    """Allows the user to insert or delete students."""
    while True:
        action = input("Type 'add' to add a student, 'delete' to delete a student, 'list' to list students, or 'exit' to exit: ").lower()
        if action == 'add':
            ask_student_details()
        elif action == 'delete':
            delete_student()
        elif action == 'list':
            list_students()
        elif action == 'exit':
            break
        else:
            print("Invalid choice, please try again.")
