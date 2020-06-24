class Student:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
    
    def display_student(self):
        print(f"Name: {self.first_name}, age: {self.last_name}")

