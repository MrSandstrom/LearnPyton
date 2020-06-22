#!/usr/bin/env python3

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display_message(self):
        print(f"Hello {self.name}!, You are {self.age} years old")

        
#person = Person("Jörgen", 48)
person = Person(age=48, name="Jörgen")
person.display_message()

print(person.name)

