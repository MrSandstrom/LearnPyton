#!/usr/bin/env python3

first_name = "Jörgen"
last_name = "Sandström"
address = "Brännås Backe"
address_number = 8
address = address + " " + str(address_number)

print('Output: ' + address + "\b9")

my_full_name = "JörgenSandström"
my_new_full_name = my_full_name[:6] + " " + my_full_name[6:]

print ("My full name: " + my_new_full_name)

print("First name: " + "\n" +"\t" + "\'" + "\\" + "first_name" + "\'")

# check string immutable
print(id(first_name))
first_name += last_name
print(id(first_name))