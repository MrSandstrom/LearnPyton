#!/usr/bin/env python3

import os
from student import Student

menu_options = ["A - Add Student", "V - View Stundent(s)", "R - Remove Student", "E - Edit Student", "Q - Quit"]

students_list = []
students_list.append(Student(first_name="Jörgen", last_name="Sandström"))
students_list.append(Student(first_name="Ludwig", last_name="Sandström"))


def add_student():
    print("-- Add a student --")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    students_list.append(Student(first_name, last_name))
    


def list_students():
    print("-- List all students --")
    for item in students_list:
        print(f"Student: {item.first_name} {item.last_name}")    


def find_student():
    print("-- Search for a stundent --")
    search_first_name = input("Enter first name: ")
    search_last_name = input("Enter last name: ")
    selected_student = ""
    for student in students_list:
        if student.first_name == search_first_name and student.last_name == search_last_name:
            selected_student = student
            break
    return selected_student


def remove_student():
    found_student = find_student()
    if (found_student == ""):
        print("Sorry, cannot find the person, try again...")
    else:
        print(f"Removing student: {found_student.first_name} {found_student.last_name}")
        students_list.remove(found_student)

def edit_student():
    found_student = find_student()
        
    if (found_student == ""):
        print("Sorry, cannot find the person, try again...")
    else:
        print(f"Found student: {found_student.first_name} {found_student.last_name}")
        updated_first_name = input("Enter the new first name: ")
        updated_last_name = input("Enter the new last name: ")        
        
        students_list.remove(found_student)
        students_list.append(Student(first_name=updated_first_name, last_name=updated_last_name))
        

while True:
    for item in menu_options:
        print(item)
    user_input = input("Choose your option: ")
    
    if user_input.upper() == "A":
        add_student()        
    elif user_input.upper() == "V":    
        list_students()
    elif user_input.upper() == "E":
        edit_student()
    elif user_input.upper() == "Q":        
        break
    elif user_input.upper() == "R":
        remove_student()
    elif user_input.upper() == "F":
        find_student()
    elif user_input.upper() == "C":
        os.system('cls') # Experimental, think this only works in windows
    else:
        print("Not a vaild option")

