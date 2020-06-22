#!/usr/bin/env python3


def add(value_1, value_2):
    result = value_1 + value_2
    print("Result: " + str(result))


add(5, 6)


def number(number=10):
    result = number * 5
    print("Result: " + str(result))


number()
number(25)


def fullName(first_name, last_name, age):
    summary = "Name: " + first_name + " " + last_name + "\nAge: " + str(age)
    return summary


print(fullName("Jörgen", "Sandström", 48))
