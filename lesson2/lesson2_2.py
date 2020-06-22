#!/usr/bin/env python3

import random

guessing = True
number_to_guess = 3

while(guessing):
    random_number = random.randint(0, 10)
    if random_number == number_to_guess:
        print("Correct number 4")
        guessing = False
    else:
        print(random_number)