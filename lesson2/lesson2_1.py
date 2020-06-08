#!/usr/bin/env python3

my_list = ["name", "last_name", "volvo"]

#print(type(my_list))
#print(len(my_list))
#print(my_list[0])

my_list.append("cars")
print(my_list)

my_list.remove("last_name")
print(my_list)

my_list.clear()
print(my_list)

my_string = "Hello"
my_string = "Hello again"

print(my_string)


my_integer_list = [1,2,3,4,5,6,7,8,9]
for item in my_integer_list:
    print(item)


index = 3

while (index < 10):
    print(index)
    index +=1