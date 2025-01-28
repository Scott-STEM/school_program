school_subjects = []

def insert_subject():
    """Asks the user to insert subjects."""
    subject = input("Please list a subject that you would like to be added to the list of school subjects: ")
    school_subjects.append(subject)
    return(f"{subject} has been added to the list.")  # Directly print the message

def delete_subject():
    """Asks the user to delete a subject from the list."""
    if not school_subjects:
        return("There are no subjects to delete.")
    else:
        return("Subjects:")
        for i, subject in enumerate(school_subjects):
            return(f"{i + 1}. {subject}")
        
        choice = int(input("Enter the number of the subject you want to delete: "))
        if 1 <= choice <= len(school_subjects):
            deleted_subject = school_subjects.pop(choice - 1)
            return(f"{deleted_subject} has been deleted.")
            return("Updated list of subjects:", school_subjects)
        else:
            return("Invalid choice, please try again.")

def in_del_sub():
    """This asks the user to insert a new subject or delete a subject. When exit is typed, a full list of subjects are returned."""
    while True:
        action = input("Would you like to 'insert' a new subject or 'delete' an existing one? Enter 'back' to return to the previous menu: ").lower()
        if action == 'insert':
            subject = insert_subject()
            print(f"{subject} has now been added.")
        elif action == 'delete':
            delete_subject()
        elif action == 'back':
            break
        else:
            return("Invalid option. Please type 'insert' or 'delete'.")

    return("Final list of subjects:", school_subjects)
