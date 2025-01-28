import students

sch_classes = []

def ins_sch_class_name():
    sch_class_name = input("Input a name for your class: ")
    sch_classes.append(sch_class_name)
    print(f"{sch_class_name} has been added.")

def del_sch_class_name():
    if not sch_classes:
        print("There are no classes to delete.")
    else:
        print("Classes:")
        for i, classes in enumerate(sch_classes):
            print(f"{i + 1}. {classes}")

        choice = int(input("Enter the number of the class you want to delete: "))
        if 1 <= choice <= len(sch_classes):
            deld_sch_class_name = sch_classes.pop(choice - 1)
            print(f"{deld_sch_class_name} has been deleted.")
        else:
            print("Invalid choice, please try again.")

def assign_students(students, sch_classes):
    # Initialize the dictionary to store class assignments
    class_assignments = {cls: [] for cls in sch_classes}
    
    for i, student in enumerate(students):
        # Your logic here to assign students to classes
        pass

    return class_assignments

def class_menu():
    sch_classes = ["Math", "Science", "History"]  # Define your classes
    assign_students(students.students_list, sch_classes)

class_menu()