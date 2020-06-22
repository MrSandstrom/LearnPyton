#!/usr/bin/env python3

### For loop 
my_forloop_integer_list = [1,2,3,4,5,6,7,8,9]
#my_forloop_integer_list.reverse()

#for n in my_forloop_integer_list:
#    print(n)

for n in reversed(my_forloop_integer_list):
    print(n)




### While loop 
my_integer_list = [1,2,3,4,5,6,7,8,9]

while_list_size = len(my_integer_list)
start_state = True


while (start_state):
    print(while_list_size)
    while_list_size -= 1
    if (while_list_size == 0):
        start_state = False




    