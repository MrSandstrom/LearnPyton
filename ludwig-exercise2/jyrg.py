def legal_status(age):    
    if age > 0 and age <= 17:
        return "Minor"
    elif age >= 18 and age <= 20:
        return "Adult"
    elif age >= 21 and age <= 30:
        return "Alcohol"
    elif age >= 31 and age <= 34:
        return "Senator"
    else:
        return "President"

inputAge = int(input("Your age: "))
print(legal_status(inputAge))