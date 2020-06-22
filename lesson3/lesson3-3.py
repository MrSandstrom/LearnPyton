#!/usr/bin/env python3


def add(value_1, value_2):
    return value_1 + value_2
    
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

try:
    first_input = int(first_number)
    second_input = int(second_number)
    result = add(first_input, second_input)
    print(f"The result is: {result}")
except:
    print("Invalid inputs")
finally:
    print(f"Program finished, the inputs were {first_input} and {second_input}")
