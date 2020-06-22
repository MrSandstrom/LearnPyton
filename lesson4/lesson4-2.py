#!/usr/bin/env python3

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name="", age=0, program=""):
        Person.__init__(self, name, age)
        self.program = program
    
    def display_student(self):
        print(f"Name: {self.name}, age: {self.age} program: {self.program}")


student = Student("Jörgen", 48, "Engineering")
student.display_student()
        


