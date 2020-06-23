#!/usr/bin/env python3

import os
from student import Student



menu_options = ["A - Add Student", "V - View Stundent(s)", "Q - Quit"]

students_list = []
students_list.append(Student(name="Jörgen", age=48))
students_list.append(Student(name="Ludwig", age=18))


def list_students():
    for item in students_list:
        print(f"Student: {item.name} age: {item.age}")

    for index, item in enumerate(students_list):
        print(index, item.name)
        



while True:
    for item in menu_options:
        print(item)
    user_input = input("Choose your option: ")
    if user_input.upper() == "A":
        print("Add Student")        
    elif user_input.upper() == "V":
        print("View")
        list_students()
    elif user_input.upper() == "Q":
        print("Quit")        
        break
    elif user_input.upper() == "C":
        os.system('cls')
    else:
        print("Not a vaild option")





