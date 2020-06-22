#!/usr/bin/env python3

def my_function():
    my_variable = 5

    def inner_function():
        nonlocal my_variable
        my_variable = 7
        print(my_variable)
    
    inner_function()
    return my_variable


print(my_function())

