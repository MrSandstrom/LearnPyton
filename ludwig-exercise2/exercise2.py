def legal_status(age): 
    
    if age > 0 and age <= 17:
        return age and print("Minor")
    elif age >= 18 and age <= 20:
        return age and print("Adult")
    elif age >= 21 and age <= 30:
        return age and print("Alcohol")
    elif age >= 31 and age <= 34:
        return age and print("Senator")
    else:
        return age and print("President")

inputAge = int(input("Your age: "))
the_age = legal_status(inputAge)