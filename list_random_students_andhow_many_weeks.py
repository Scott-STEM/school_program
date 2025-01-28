""" Asks the teacher how many weeks of random Students would she/he would like to produce. """
from random import choice
import students
import sch_class
school_class_y = []
school_class_n = []



def select_student():
    """ Randomly selects a student from stu_n and then appends this student to stu_y"""
    global school_class_y, school_class_n
    
    if not school_class_n:  # If no students left to choose from, reset the lists
        school_class_n, school_class_y = school_class_y, []
    
    student = choice(school_class_n)  # Select a random student from the pool
    school_class_n.remove(student)  # Remove selected student from the 'not had a turn' list
    school_class_y.append(student)  # Add selected student to the 'had a turn' list
    
    return student


            
    
