#!/usr/bin/env python3

import os
from student import Student



menu_options = ["A - Add Student", "V - View Stundent(s)", "E - Edit Student","Q - Quit"]

students_list = []
students_list.append(Student(first_name="Jörgen", last_name="Sandström"))
students_list.append(Student(first_name="Ludwig", last_name="Sandström"))


def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    students_list.append(Student(first_name, last_name))
    print(f"New Student added.")



def list_students():
    for item in students_list:
        print(f"Student: {item.first_name} {item.last_name}")
    #for index, item in enumerate(students_list):
    #    print(f"Index: {index} Name: {item.first_name} {item.last_name}")

def find_student():
    search_first_name = input("Enter first name: ")
    search_last_name = input("Enter last name: ")
    selected_student = ""
    for student in students_list:
        if student.first_name == search_first_name and student.last_name == search_last_name:
            selected_student = student
            break
    
    if (selected_student == ""):
        print("Sorry, cannot find the person, try again...")
    else:
        print(f"Found student: {selected_student.first_name} {selected_student.last_name}")
    

def edit_student():
    print("Enter some data to be able to find the student you want to edit!")
    search_first_name = input("Enter first name: ")
    selected_student = ""
    for student in students_list:
        if student.first_name == search_first_name:            
            selected_student = student
            break
        
    if (selected_student == ""):
        print("Sorry, cannot find the person, try again...")
    else:
        print(f"Found student: {selected_student.first_name}")
        updated_first_name = input("Enter the new first name: ")        
        
        students_list.remove(selected_student)
        students_list.append(Student(first_name=updated_first_name, last_name="Jalla Jalla"))
        

    






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
    elif user_input.upper() == "F":
        find_student()
    elif user_input.upper() == "C":
        os.system('cls')
    else:
        print("Not a vaild option")





