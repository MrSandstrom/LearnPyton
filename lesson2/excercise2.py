#!/usr/bin/env python3

# 1
hello_world_string = "Hello World"
new_hello_world_string = hello_world_string[:5] + "," + hello_world_string[5:]
#print(new_hello_world_string)

# 2
new_hello_world_string = hello_world_string[:5] + "\n" + "," + hello_world_string[5:]
#print(new_hello_world_string)

# 3 range
value = range(len(hello_world_string))
#for item in value:
    #print (hello_world_string[item])

print("------------")

# 4
my_value = len(hello_world_string)
loop = True
counter = 0

while (loop):
    if (counter < my_value):
        print(hello_world_string[counter])
        counter += 1                
    else:
        loop = False




