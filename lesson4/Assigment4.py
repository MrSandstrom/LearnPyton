#!/usr/bin/env python3

import os
#from student import Student

class Student:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
    
    def display_student(self):
        print(f"Name: {self.first_name}, age: {self.last_name}")


menu_options = ["A - Add Student", "V - View Stundent(s)", "R - Remove Student", "E - Edit Student", "Q - Quit"]

students_list = []
# populate with some inital values with well know Frölunda Indians players :-)
students_list.append(Student(first_name="Henrik", last_name="Lundqvist"))
students_list.append(Student(first_name="John", last_name="Klingberg"))
students_list.append(Student(first_name="Henrik", last_name="Tömmernäs"))
students_list.append(Student(first_name="Ryan", last_name="Lasch"))
students_list.append(Student(first_name="Jan", last_name="Mursak"))
students_list.append(Student(first_name="Victor", last_name="Stålberg"))


def add_student():
    print("-- Add a student --")
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        students_list.append(Student(first_name, last_name))
    except:
        print("Invalid values - Should however not happen since not only handling strings, only here since it was in the instructions")
    finally:
        print(f"Student: {first_name} {last_name} added to inventory")
    

def list_students():
    print("-- List all students --")
    for item in students_list:
        print(f"Student: {item.first_name} {item.last_name}")    


def find_student():    
    search_first_name = input("Enter first name: ")
    search_last_name = input("Enter last name: ")
    selected_student = ""
    for student in students_list:
        if student.first_name == search_first_name and student.last_name == search_last_name:
            selected_student = student
            break
    return selected_student


def remove_student():
    print("-- Remove a stundent --")
    found_student = find_student()
    if (found_student == ""):
        print("Sorry, cannot find the person, try again...")
    else:
        print(f"Removing student: {found_student.first_name} {found_student.last_name}")
        students_list.remove(found_student)


def edit_student():
    print("-- Edit a stundent --")
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
    elif user_input.upper() == "R":
        remove_student()     
    elif user_input.upper() == "Q":        
        break
    elif user_input.upper() == "C":
        os.system('cls') # Experimental, think this only works in windows
    else:
        print("Not a vaild option")

