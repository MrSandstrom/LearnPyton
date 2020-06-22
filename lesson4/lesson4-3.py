#!/usr/bin/env python3

def my_function():
    global my_variable
    print(my_variable)

    def inner_fuction():
        global my_variable
        my_variable = 0
        print(my_variable)

    inner_fuction()

    

my_variable = 5
my_function()
print(my_variable)

