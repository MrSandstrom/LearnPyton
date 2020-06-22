#!/usr/bin/env python3

# string formatting
name = "Jörgen Sandström"
age = 48

print("My name is %s and I'm %d years old" % (name, age))
print("My name is {0} and I'm {1} years old".format(name,age))
print(f"My anme is {name} and I'm {age} years old")

x = 5
y = 7

print(f"{x} plus {y} equals {x+y}")


my_input = input("Enter your name:")

try:    
    number = int(my_input)
except:
    print("Invalid input")
finally:
    print(my_input)

