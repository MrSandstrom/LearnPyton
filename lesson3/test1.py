#!/usr/bin/env python3


def swap_characters(name, password):
    first_name_char = name[0]    
    last_name_char = name[len(name)-1]
    first_password_char = password[0]
    last_password_char = password[len(password)-1]
    
    # char array, replace char values
    modified_name = list(name)
    modified_name[0] = first_password_char
    modified_name[len(name)-1] = last_password_char
    modified_password = list(password)
    modified_password[0] = first_name_char
    modified_password[len(password)-1] = last_name_char
    
    # back to strings
    final_name = "".join(modified_name)    
    final_password = "".join(modified_password)

    print(f"Username: {final_name} \nPassword: {final_password}")
    

    
user_name = input("Enter your user name: ")
user_password = input("Enter your password: ")

try:
    integer_user_password = int(user_password)
    swap_characters(user_name, user_password)
except:
    print("Invalid inputs")
finally:
    print(f"Program finished, the inputs were {user_name} and {user_password}")