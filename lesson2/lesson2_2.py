#!/usr/bin/env python3

import random

guessing = True
number_to_guess = 4

while(guessing):
    random_number = random.randint(0, 10)
    if random_number == number_to_guess:
        print("Correct")
        guessing = False
    else:
        print(random_number)